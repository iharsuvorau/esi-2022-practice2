from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route("ping")
def pong():
    pass


@app.route("time")
def show_time():
    pass
