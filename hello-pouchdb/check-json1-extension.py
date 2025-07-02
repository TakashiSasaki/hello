import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

try:
    cursor.execute("SELECT json_valid('{}');")
    result = cursor.fetchone()
    if result is not None:
        print("JSON1 extension is enabled.")
    else:
        print("JSON1 extension is not enabled.")
except sqlite3.OperationalError as e:
    print("JSON1 extension is not enabled:", e)
