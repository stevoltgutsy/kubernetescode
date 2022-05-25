from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Please note, This is my First Jenkins CICD-2022-04'
