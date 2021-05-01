#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c_is(text):
    return 'C ' + text.replace("_", " ")


@app.route('/python')
def python_alone():
    return "Python is cool"


@app.route('/python/<text>')
def python(text="is cool"):
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
