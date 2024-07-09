from flask import jsonify, Blueprint
from http import HTTPStatus

# This Blueprint function is used to create a new Blueprint object that represents a collection of routes.
trips_routes_blueprint = Blueprint("trip_routes", __name__)


@trips_routes_blueprint.route("/trips", methods=["GET"])
def create_trip():
    return jsonify({"message": "Trips route"}), HTTPStatus.OK
