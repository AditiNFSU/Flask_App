import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, email TEXT)''')
cursor.execute("INSERT INTO users (username, email) VALUES ('admin', 'admin@example.com')")
cursor.execute("INSERT INTO users (username, email) VALUES ('user1', 'user1@example.com')")
conn.commit()
conn.close()
