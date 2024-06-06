#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, url_for
from models import storage
import uuid

app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = "0.0.0.0"


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/3-hbnb")
def hbnb_filters(id=None):
    """Display a HTML page: 3-hbnb.html"""
    states = dict(
        [(state.id, state.name) for state in storage.all("State").values()]
    )
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    users = dict(
        [
            (user.id, user.first_name + " " + user.last_name)
            for user in storage.all("User").values()
        ]
    )
    cache_id = str(uuid.uuid4())
    return render_template(
        "3-hbnb.html",
        cache_id=cache_id,
        states=states,
        amenities=amenities,
        places=places,
        users=users,
    )


if __name__ == "__main__":
    app.run(host=host, port=port)
