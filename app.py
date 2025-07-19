import flask

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask with potential issues!'

if __name__ == '__main__':
    app.run()
