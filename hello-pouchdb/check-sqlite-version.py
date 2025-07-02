import sqlite3
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('SELECT sqlite_version();')
version = cursor.fetchone()[0]
print(f'SQLite version: {version}')
