#!/usr/bin/python3
"""
This script kicks a flask web app.

The app will be accesible on 0.0.0.0, on port 5000.

Routes:
    /: Will display 'Hello HBNB!'
    /hbnb: Will display 'HBNB'
    /c/<text>: Will display 'C ' followed by the value of the text variable
"""

# Creating an instance of the Flask web server
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Returns a message.

    When the user navigates to the root directory (http://0.0.0.0:5000/),
    the message 'Hello HBNB!' will be displayed.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns a message.

    When the user navigates to the /hbnb directory (http://0.0.0.0:5000/hbnb),
    the message 'HBNB' will be displayed.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ Shows 'C' and the content of <text> """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Shows "Python" with modified 'text'. """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """ Shows a message stating that 'n' is a number """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Renders 'number.html' with the 'n' is a number """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    # Starts the web server with host as 0.0.0.0 and port 5000
    app.run(host="0.0.0.0", port=5000)
