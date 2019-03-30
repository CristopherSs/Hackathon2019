"""Generate Database module"""
import json
from typing import Dict
from database.table_generator.table_generator import TableGenerator
from database.query_launcher import QueryLauncher
from backend.user.user import User
from backend.user.disability import Disabilities


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
    room = User(**data)
    generator.generate(room)


if __name__ == '__main__':
    config = {'user': 'root', 'password': 'password', 'database': '', 'host': ''}
    generate(config)
