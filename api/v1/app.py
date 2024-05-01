#!/usr/bin/python3
"""This is the modeule that controls the main flask application"""

from models import storage
from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from flask import make response
import os
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(exception):
    """close connection to the database"""
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """return a 404 json response"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = ox.getenv("HBNB_API_HOST")
    if not host:
        host = "0.0.0.0"
    port = os.getenv("HBNB_API_PORT")
    if not port:
        port = 5000
    app.run(host=host, port=port, threaded=True)
