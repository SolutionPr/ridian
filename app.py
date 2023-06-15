from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1 style="text-align:center;">Welcome to Ridian!</h1>'
