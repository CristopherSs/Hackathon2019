import json
import os

from Rooms.API._flask import ApplicationFlask
from Rooms.API.resources_api.api import Api
from Rooms.backend.booking.only_booking import Booking
from Rooms.backend.booking.verifier_booking import VerifierBookings
from Rooms.backend.room.room import Room
from Rooms.backend.user.user import User
from Rooms.database.condition import Condition
from Rooms.database.database import Database
from Rooms.database.query_launcher import QueryLauncher

with open(os.getcwd() + '/Rooms/database/config.json') as file:
    database = Database(QueryLauncher(json.load(file)))
with open(os.getcwd() + '/Rooms/API/resources_api/headers_jsonify.json') as file:
    headers_response_access = json.load(file)
condition1 = Condition('room_id', '=', '')
condition2 = Condition('date', '=', '')
api_booking = Api(reference=Booking, database=database, verifier=VerifierBookings([condition1, condition2], database),
                  headers=headers_response_access)
api_room = Api(Room, database, headers=headers_response_access)
api_user = Api(User, database, headers=headers_response_access)
flask = ApplicationFlask()
flask.register_url_of_resource_api(api_booking)
flask.register_url_of_resource_api(api_room)
flask.register_url_of_resource_api(api_user)
flask.run('10.28.116.159', '8080')
