"""Generate Database module"""
import json
from typing import Dict

from backend.city.city import City
from backend.disaster_department.disaster_department import DisasterDepartment
from backend.user.department import Department
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
    data = {'email': '', 'password': '', 'gender': '', 'name': '', 'last_name': '',
            'disability': Disabilities.NONE}
    user = User(**data)
    generator.generate(user, True)
    data = {'city_name': '', 'city_id': 0}
    city = City(**data)
    generator.generate(city, True)

    data = {'email': '', 'password': '', 'area': Areas.FIREFIGHTERS, 'city_id': 0}
    department = Department(**data)
    generator.generate(department, True)

    data = {'disaster_name': ''}
    disaster = Disaster(**data)
    generator.generate(disaster, True)

    data = {'advice': '', 'disaster_id': 0}
    protocol = Protocol(**data)
    generator.generate(protocol, True)

    query = 'CREATE TABLE IF NOT EXISTS DisasterDepartment (disaster_id INT(5) NOT NULL, department_id ' \
            'INT(5) NOT NULL, CONSTRAINT FOREIGN KEY (disaster_id) REFERENCES disaster(disaster_id) ON DELETE ' \
            'CASCADE ON UPDATE RESTRICT, CONSTRAINT FOREIGN KEY (department_id) REFERENCES department(department_id) ' \
            'ON DELETE CASCADE ON UPDATE RESTRICT)'
    launcher.launch(query)

    database = Database(launcher)

    user_data = {'email': 'sebas', 'password': '123','gender': 'male',
                 'name': 'Sebastian', 'last_name': 'Medrano', 'disability': Disabilities.NONE}
    user = User(**user_data)
    database.save_data(user)
    city_data = {'city_name': 'Cochabamba'}
    city = City(**city_data)
    city = database.save_data(city)
    department_data = {'email': 'police123', 'password': '1234', "area": Areas.POLICE, 'city_id': city.city_id}
    department = Department(**department_data)
    department = database.save_data(department)
    disaster_data = {'disaster_name': 'fire'}
    disaster = Disaster(**disaster_data)
    disaster = database.save_data(disaster)
    protocol_data = {'advice': 'evacuate', 'disaster_id': disaster.disaster_id}
    protocol = Protocol(**protocol_data)
    database.save_data(protocol)

    disaster_department_data = {'disaster_id': disaster.disaster_id, 'department_id': department.department_id}
    disaster_department = DisasterDepartment(**disaster_department_data)
    database.save_data(disaster_department)


if __name__ == '__main__':
    config = {'user': 'root', 'password': 'password', 'database': '', 'host': ''}
    generate(config)
