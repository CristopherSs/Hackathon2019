"""department module"""
from backend.user.user_model import UserModel
from database.i_table import Table
from dataclasses import dataclass
from backend.department.areas import Areas


@dataclass
class Department(Table, UserModel):
    area: Areas
    city_id: int
    department_id: int = 0

    def get_primary_key(self) -> str:
        return 'department_id'

    def get_class_name(self) -> str:
        return self.__class__.__name__
