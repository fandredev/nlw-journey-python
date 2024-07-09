from flask import jsonify, Blueprint, request
from http import HTTPMethod

from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder

from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository

from src.models.settings.db_connection_handler import db_connection_handler


# This Blueprint function is used to create a new Blueprint object that represents a collection of routes.
trips_routes_blueprint = Blueprint("trip_routes", __name__)


@trips_routes_blueprint.route("/trips", methods=["POST"])
def create_trip():
    connection = db_connection_handler.get_connection()
    trip_repository = TripsRepository(connection)
    emails_repository = EmailsToInviteRepository(connection)

    controller_trip_creator = TripCreator(trip_repository, emails_repository)

    response = controller_trip_creator.create(request.json)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_blueprint.route("/trips/<trip_id>", methods=["GET"])
def detail_trip(trip_id: str):
    connection = db_connection_handler.get_connection()
    trip_repository = TripsRepository(connection)

    controller_trip_finder = TripFinder(trip_repository)

    # The request.view_args["trip_id"] is a dictionary that contains the URL parameters.
    response = controller_trip_finder.find_trip_details(trip_id)

    return jsonify(response["body"]), response["status_code"]
