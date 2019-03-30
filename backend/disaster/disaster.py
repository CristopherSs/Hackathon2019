""""Disaster module"""
from dataclasses import dataclass
from API.request_querys.request import Query
from backend.department.department import Department
from database.i_table import Table


@dataclass
class Disaster(Table):
    disaster_name: str
    department_id: int
    disaster_id: int = 0

    def get_primary_key(self) -> str:
        return 'disaster_id'

    def get_class_name(self) -> str:
        return self.__class__.__name__
