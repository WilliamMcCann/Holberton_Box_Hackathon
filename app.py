from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/phone_numbers', methods=['GET'])
def OAuth2():
    r = requests.get("http://example.com/foo/bar")
    return 'Folder data response.'
