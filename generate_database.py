"""Generate Database module"""
import json
from typing import Dict

from backend.city.city import City
from backend.department.department import Department
from backend.disaster.disaster import Disaster
from backend.protocol.protocol import Protocol
from database.database import Database
from database.table_generator.table_generator import TableGenerator
from database.query_launcher import QueryLauncher
from backend.user.user import User
from backend.user.disability import Disabilities
from backend.department.areas import Areas


def generate(config: Dict) -> None:
    """
    generates the tables
    :return: None
    """
    query = 'CREATE DATABASE IF NOT EXISTS hackathon;'
    launcher = QueryLauncher(config)
    launcher.launch(query)
    with open('database/config.json', 'r') as file:
        config = json.load(file)
    launcher.change_config_values(config)
    generator = TableGenerator(launcher)
    data = {'user_id': '', 'password': '', 'name': '', 'last_name': '', 'disability': Disabilities.NONE}
    user = User(**data)
    generator.generate(user)
    data = {'city_name': '', 'city_id': 0}
    city = City(**data)
    generator.generate(city, True)

    data = {'user_name': '', 'password': '', 'area': Areas.FIREFIGHTERS, 'city_id': 0, 'department_id': 0}
    department = Department(**data)
    generator.generate(department, True)

    data = {'disaster_name': '', 'department_id': 0}
    disaster = Disaster(**data)
    generator.generate(disaster, True)

    data = {'advice': '', 'disaster_id': 0}
    protocol = Protocol(**data)
    generator.generate(protocol, True)

    database = Database(launcher)

    """disaster_data = {'disaster_name': 'fire', 'department_id': 1}
    disaster = Disaster(**disaster_data)
    disaster = database.save_data(disaster)
    protocol_data = {'advice': 'evacuate', 'disaster_id': disaster.disaster_id}
    protocol = Protocol(**protocol_data)
    database.save_data(protocol)
    city_data = {'city_name': 'Cochabamba'}
    city = City(**city_data)
    city = database.save_data(city)

    department_data = {'user_name': 'police123', 'password': '1234', "area": Areas.POLICE, 'city_id': city.city_id}
    department = Department(**department_data)
    database.save_data(department) """


if __name__ == '__main__':
    config = {'user': 'root', 'password': 'password', 'database': '', 'host': ''}
    generate(config)
