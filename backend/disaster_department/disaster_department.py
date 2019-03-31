"""disaster department link module"""
from dataclasses import dataclass
from database.i_table import Table


@dataclass
class DisasterDepartment(Table):
    disaster_id: int
    department_id: str

    def get_primary_key(self) -> str:
        return ''

    def get_class_name(self) -> str:
        return self.__class__.__name__
