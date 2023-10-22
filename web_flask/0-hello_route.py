#!/usr/bin/python3
# A script that starts a Flask web application.

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define a route for the root URL ('/') and allow trailing slashes
@app.route('/', strict_slashes=False)
# Function to return “Hello HBNB!” at root URL
def hello_hbnb():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
