#!/usr/bin/python3
""" Script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def domainFunction():
    """ Responsible of the domain route, displays a message """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnbFunction():
    """ Responsible of the /hbhb route, displays a message """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def textCFunction(text):
    """ Responsible of the /C/text route, displays text """
    text = text.replace('_', ' ')
    return ("C {}".format(text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def textPFunction(text='is cool'):
    """ Responsible of the /python/text route, displays text """
    text = text.replace('_', ' ')
    return ("Python {}".format(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
