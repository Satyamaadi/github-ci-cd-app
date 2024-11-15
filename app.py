from flask import Flask

app = Flask(__name__)

# Define the home route
@app.route('/')
def hello_world():
    return 'Hello, World! I am a ci-cd app - just added cd and runner'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
