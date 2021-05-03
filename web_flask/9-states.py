#!/usr/bin/python3
""" Start flask app web, using storage engine """
from models import storage
from flask import render_template
from models.state import State
from models.city import City
from flask import Flask
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def index(id=None):
    """ Index to display lists """
    states = storage.all(State)
    cities = storage.all(City)
    if id is None:
        return render_template('7-states_list.html', states=states)
    else:
        exist = 0  # 0 if not, 1 if yes
        state_name = ""
        for state in states.values():
            if state.id == id:
                exist += 1
                state_name = state.name
        return render_template('9-states.html', states=states, cities=cities,
                               id=id, exist=exist, state_name=state_name)


@app.teardown_appcontext
def close(states):
    ''' Close the connection with db '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
