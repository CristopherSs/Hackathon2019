""""protocol module"""
from dataclasses import dataclass
from database.i_table import Table


@dataclass
class Protocol(Table):
    advice: str
    disaster_id: int
    protocol_id: int = 0

    def get_primary_key(self) -> str:
        return 'protocol_id'

    def get_class_name(self) -> str:
        return self.__class__.__name__
