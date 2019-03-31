import json

from API._flask import ApplicationFlask
from API.resources_api.api import Api
from backend.city.city import City
# from backend.department.department import Department
from backend.login import LoginVerifier
from backend.user.user import User
from database.database import Database
from database.query_launcher import QueryLauncher

with open('database/config.json', 'r') as file:
    config = json.load(file)
launcher = QueryLauncher(config)
database = Database(launcher)
with open('API/resources_api/headers_jsonify.json', 'r') as file:
    headers = json.load(file)
api_user = Api(User, database, headers)
api_city = Api(City, database, headers)
flask_ = ApplicationFlask()
flask_.register_url_of_resource_api(api_user)
flask_.register_url_of_resource_api(api_city)
flask_.run('172.20.80.27', '8080')
