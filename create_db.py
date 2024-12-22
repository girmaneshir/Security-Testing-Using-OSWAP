import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('demo_app.db')

# Create a new SQLite cursor
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_inputs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input TEXT NOT NULL
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()