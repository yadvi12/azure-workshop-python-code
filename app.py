from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h3>Hello, Yadvi!</h3>    <img src='https://myimagest.blob.core.windows.net/mycimage/badge.png'/>"
