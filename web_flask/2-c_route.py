#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
import sys

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def domainFunction():
    """
    Responsible of the domain route, displays a message
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnbFunction():
    """
    Responsible of the /hbhb route, displays a message
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def textFunction(text):
    """
    Responsible of the /C/text route, displays text
    """
    text = text.replace('_', ' ')
    return ("C {}".format(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
