#!/usr/bin/python3
""" Configure the filters view for airbnb """
from flask import Flask, escape, render_template
import models
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """ Lists all states """
    states = {}
    amenities = []
    all_states = models.storage.all(State)
    all_amenities = models.storage.all(Amenity)

    for key, value in all_amenities.items():
        amenities.append(value.name)
    amenities.sort()

    for key, value in all_states.items():
        states[value.name] = value

    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def close_db_session(states):
    """ Close the db session """
    if states:
        storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
