""""Disaster module"""
from dataclasses import dataclass
from database.i_table import Table


@dataclass
class Disaster(Table):
    disaster_name: str
    disaster_id: int = 0

    def get_primary_key(self) -> str:
        return 'disaster_id'

    def get_class_name(self) -> str:
        return self.__class__.__name__
