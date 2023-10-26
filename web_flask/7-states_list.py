#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from flask import Flask, render_template
from models import storage
from models import state

# Create an instance of Flask
app = Flask(__name__)


# Define a route for /states_list with strict_slashes=False
@app.route('/states_list', strict_slashes=False)
def states_list():
    # Get all the states from the storage engine and sort them by name
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    # Render a HTML template with the states list
    return render_template('7-states_list.html', states=states)


# Define a method to handle app teardown
@app.teardown_appcontext
def teardown_appcontext(exception):
    # Close the current SQLAlchemy session
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
