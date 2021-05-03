#!/usr/bin/python3
""" Start flask app web, using storage engine """
from models import storage
from flask import render_template
from models.state import State
from models.city import City
from flask import Flask
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def index():
    """ Index to display lists """
    states = storage.all(State)
    cities = storage.all(City)
    # states_list = {}
    # for key, value in states.items():
    #     states_list[value.name] = value
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


@app.teardown_appcontext
def close(states):
    ''' Close the connection with db '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
