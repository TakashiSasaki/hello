import sqlite3
import tempfile
import os
import signal
from wsgiref.simple_server import make_server, WSGIServer
from eralchemy import render_er

MIME_TYPES = {
    '.sql': 'text/plain',
    '.txt': 'text/plain',
    '.html': 'text/html',
    '.htm': 'text/html',
    '.css': 'text/css',
    '.webp': 'image/webp',
}

class TimeoutWSGIServer(WSGIServer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timeout = 1

def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, path.lstrip('/'))

    if method == 'OPTIONS':
        start_response('200 OK', [
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', 'POST, GET, OPTIONS'),
            ('Access-Control-Allow-Headers', 'Content-Type'),
        ])
        return [b'']

    if method == 'GET':
        file_ext = os.path.splitext(file_path)[1]
        mime_type = MIME_TYPES.get(file_ext)

        if mime_type and os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
            start_response('200 OK', [
                ('Access-Control-Allow-Origin', '*'),
                ('Content-Type', mime_type),
                ('Content-Length', str(len(content))),
            ])
            return [content]
        else:
            start_response('404 Not Found', [
                ('Access-Control-Allow-Origin', '*'),
                ('Content-Type', 'text/plain'),
            ])
            return [b"File not found"]

    if method == 'POST':
        try:
            content_length = int(environ.get('CONTENT_LENGTH', 0))
            body = environ['wsgi.input'].read(content_length).decode('utf-8')

            if not body.strip():
                raise ValueError("Received SQL query is empty.")

            temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
            temp_db_name = temp_db.name
            temp_db.close()

            temp_webp = tempfile.NamedTemporaryFile(suffix=".webp", delete=False)
            temp_webp_name = temp_webp.name
            temp_webp.close()

            connection = sqlite3.connect(temp_db_name)
            cursor = connection.cursor()
            cursor.executescript(body)
            connection.commit()
            connection.close()
            del connection, cursor  # リソースを明示的に解放

            render_er(f"sqlite:///{temp_db_name}", temp_webp_name)

            with open(temp_webp_name, "rb") as webp_file:
                webp_data = webp_file.read()

            start_response('200 OK', [
                ('Access-Control-Allow-Origin', '*'),
                ('Content-Type', 'image/webp'),
                ('Content-Length', str(len(webp_data))),
            ])
            return [webp_data]

        except Exception as e:
            error_message = f"Error: {e}"
            start_response('500 Internal Server Error', [
                ('Access-Control-Allow-Origin', '*'),
                ('Content-Type', 'text/plain; charset=utf-8'),
            ])
            return [error_message.encode('utf-8')]

    start_response('405 Method Not Allowed', [
        ('Access-Control-Allow-Origin', '*'),
        ('Content-Type', 'text/plain'),
    ])
    return [b"Only POST and GET methods are supported."]

def run_server():
    global server
    port = 18080
    server = make_server('', port, application, server_class=TimeoutWSGIServer)
    print(f"Serving on port {port}... (Press Ctrl+C to stop)")

    try:
        while True:
            server.handle_request()
    except KeyboardInterrupt:
        print("\nShutting down server gracefully...")
        server.shutdown()
        print("Server stopped.")

if __name__ == '__main__':
    run_server()
