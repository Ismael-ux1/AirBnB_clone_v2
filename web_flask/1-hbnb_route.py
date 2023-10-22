#!/usr/bin/python3
"""
This scripts kiks a flask web app.

The app will be accesible on 0.0.0.0, on port 5000.

Routs:
    /: Will display 'Hello HBNB!'
    /hbnb: Will display 'HBNB'
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


if __name__ == "__main__":
    # Starts the web server with host as 0.0.0.0 and port 5000
    app.run(host="0.0.0.0", port=5000)
