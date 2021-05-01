#!/usr/bin/python3
''' Turn on flask web app with multiple routes '''
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    ''' First page to load when entering 0:5000 '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''' hbnb path show HBNB '''
    return "HBNB"


@app.route('/c/<text>')
def c_is(text):
    ''' text: used to print C + /text '''
    return 'C ' + text.replace("_", " ")


@app.route('/python')
def python_alone():
    ''' route python to show python is cool '''
    return "Python is cool"


@app.route('/python/<text>')
def python(text):
    ''' route python to show the text user passed as subpath '''
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    ''' Prints <number> is a number if is a number.'''
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
