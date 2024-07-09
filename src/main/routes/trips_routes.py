from flask import jsonify, Blueprint, request
from http import HTTPMethod

from src.controllers.trip_creator import TripCreator


from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository

from src.models.settings.db_connection_handler import db_connection_handler


# This Blueprint function is used to create a new Blueprint object that represents a collection of routes.
trips_routes_blueprint = Blueprint("trip_routes", __name__)


@trips_routes_blueprint.route("/trips", methods=[HTTPMethod.POST])
def create_trip():
    connection = db_connection_handler.get_connection()
    trip_repository = TripsRepository(connection)
    emails_repository = EmailsToInviteRepository(connection)

    controller_trip_creator = TripCreator(trip_repository, emails_repository)

    response = controller_trip_creator.create(request.json)

    return jsonify(response["body"]), response["status_code"]
