from flask import Flask, request, render_template_string
import os
import sqlite3

app = Flask(__name__)

# Vulnerable route: SQL Injection
@app.route('/user/<username>')
def get_user(username):
    # Directly inserting user input into SQL query without sanitization
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return f"User details: {user}"

# Vulnerable route: Cross-Site Scripting (XSS)
@app.route('/search')
def search():
    query = request.args.get('q')  # Unsanitized input directly rendered in the response
    return f"<h1>Search Results for: {query}</h1>"

# Vulnerable route: Remote Code Execution (RCE)
@app.route('/run')
def run_command():
    cmd = request.args.get('cmd')  # Accepting user input as a system command
    result = os.popen(cmd).read()
    return f"Command Output: {result}"

# Vulnerable route: Insecure Template Rendering
@app.route('/template')
def render_template():
    template = request.args.get('template')  # Accepting raw user input for templates
    return render_template_string(template)

if __name__ == "__main__":
    # Enabling debug mode in production is a vulnerability
    app.run(debug=True)
