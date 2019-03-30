"""City module"""
from dataclasses import dataclass
from database.i_table import Table


@dataclass
class City(Table):
    city_name: str
    city_id: int = 0

    def get_primary_key(self) -> str:
        return 'city_id'

    def get_class_name(self) -> str:
        return self.__class__.__name__
