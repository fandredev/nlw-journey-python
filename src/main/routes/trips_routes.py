from flask import jsonify, Blueprint, request

from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirm import TripConfirm

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.participant_confirm import ParticipantConfirm

from src.controllers.activity_creator import ActivityCreator
from src.controllers.activity_finder import ActivityFinder


from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.activities_repository import ActivitiesRepository

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

    response = controller_trip_finder.find_trip_details(trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_blueprint.route("/trips/<trip_id>/confirm", methods=["GET"])
def confirm_trip_link(trip_id: str):
    connection = db_connection_handler.get_connection()
    trip_repository = TripsRepository(connection)

    controller_trip_confirm = TripConfirm(trip_repository)

    response = controller_trip_confirm.confirm(trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_blueprint.route("/trips/<trip_id>/links", methods=["POST"])
def create_link(trip_id: str):
    connection = db_connection_handler.get_connection()
    link_repository = LinksRepository(connection)

    controller_link_creator = LinkCreator(link_repository)

    response = controller_link_creator.create(request.json, trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_blueprint.route("/trips/<trip_id>/links", methods=["GET"])
def find_trip_link(trip_id: str):
    connection = db_connection_handler.get_connection()
    links_repository = LinksRepository(connection)

    controller_link_finder = LinkFinder(links_repository)

    response = controller_link_finder.find(trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_blueprint.route("/trips/<trip_id>/invites", methods=["POST"])
def invite_to_trip(trip_id: str):
    connection = db_connection_handler.get_connection()
    emails_repository = EmailsToInviteRepository(connection)
    participants_repository = ParticipantsRepository(connection)

    controller_participant_creator = ParticipantCreator(
        participants_repository, emails_repository
    )

    response = controller_participant_creator.create(request.json, trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_blueprint.route("/trips/<trip_id>/activities", methods=["POST"])
def create_activity(trip_id: str):
    connection = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(connection)

    controller_activity_creator = ActivityCreator(activities_repository)

    response = controller_activity_creator.create(request.json, trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_blueprint.route("/trips/<trip_id>/activities", methods=["GET"])
def get_trip_activities(trip_id: str):
    connection = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(connection)

    controller_activity_finder = ActivityFinder(activities_repository)

    response = controller_activity_finder.find_from_trip(trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_blueprint.route("/trips/<trip_id>/participants", methods=["GET"])
def get_trip_participants(trip_id: str):
    connection = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(connection)

    controller_participant_finder = ParticipantFinder(participants_repository)

    response = controller_participant_finder.find_participants_from_trip(trip_id)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_blueprint.route(
    "/participants/<participant_id>/confirm", methods=["PATCH"]
)
def confirm_participant(participant_id: str):
    connection = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(connection)

    controller_participant_confirm = ParticipantConfirm(participant_repository)

    response = controller_participant_confirm.confirm(participant_id)

    return jsonify(response["body"]), response["status_code"]
