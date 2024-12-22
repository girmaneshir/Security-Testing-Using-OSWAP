from flask import Flask, request, jsonify, render_template_string
import sqlite3

app = Flask(__name__)

DATABASE = 'demo_app.db'

# Simple HTML template
HTML_TEMPLATE = """
<!doctype html>
<html>
<head><title>Flask Demo App</title></head>
<body>
    <h1>Welcome to the Flask Demo App</h1>
    <form method="POST" action="/submit">
        <input type="text" name="input" placeholder="Type something" required>
        <button type="submit">Submit</button>
    </form>
    <h2>Stored Inputs</h2>
    <ul>
        {}
    </ul>
    <a href="/vulnerable">Go to Vulnerable Page</a>
</body>
</html>
"""

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enable row access
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    inputs = conn.execute('SELECT * FROM user_inputs').fetchall()
    conn.close()

    input_list = ''.join(f'<li>{row["input"]}</li>' for row in inputs)
    return render_template_string(HTML_TEMPLATE.format(input_list))

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('input')

    # Store input in the database
    conn = get_db_connection()
    conn.execute('INSERT INTO user_inputs (input) VALUES (?)', (user_input,))
    conn.commit()
    conn.close()

    return f"You entered: {user_input}. <a href='/'>Go back</a>"

@app.route('/vulnerable')
def vulnerable():
    return """
    <h1>Vulnerable Page</h1>
    <form method="GET" action="/vulnerable">
        <input type="text" name="input" placeholder="Type something" required>
        <button type="submit">Submit</button>
    </form>
    <p>{}</p>
    """.format(request.args.get('input', ''))

if __name__ == '__main__':
    app.run(debug=True)