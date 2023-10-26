#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


# Route to display a list of states
@app.route('/states')
def states():
    """Displays a list of states.

    States are sorted by name for improved readability.
    """
    states = storage.all('State').values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>')
def state(id):
    """Displays details about a specific state and its cities.

    If the state is not found, a 404 error page is displayed.
    """
    state = storage.get('State', id)
    if state is None:
        return render_template('404.html'), 404
    else:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
