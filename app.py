from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Simulated in-memory "database"
users = {"alice": {"email": "alice@example.com"}, "bob": {"email": "bob@example.com"}}

@app.route('/')
def home():
    return 'Welcome to the Dummy API!'

@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(users)

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    if username in users:
        return jsonify({username: users[username]})
    else:
        abort(404, description="User not found")

@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or 'username' not in request.json:
        abort(400, description="Missing user data")
    username = request.json['username']
    email = request.json.get('email', f'{username}@example.com')
    users[username] = {"email": email}
    return jsonify({username: users[username]}), 201

if __name__ == '__main__':
    app.run(debug=True)
