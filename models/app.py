from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/auth')
def OAuth2():
    return 'The authentication page.'
