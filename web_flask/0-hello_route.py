#!/usr/bin/python3
"""
This script kicks off a Flask web app.

The app will be reachable on 0.0.0.0, listening on port 5000.
Routes:
    /: Will show 'Hello HBNB!'
"""
from flask import Flask
# Create a Flask application instance
app = Flask(__name__)


# Define a route for the root URL ('/') and allow trailing slashes
@app.route('/', strict_slashes=False)
# Function to return “Hello HBNB!” at root URL
def hello_hbnb():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
