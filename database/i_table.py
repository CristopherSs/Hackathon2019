"""i_table module"""
from abc import ABC, abstractmethod
from datetime import date, time
from enum import Enum


class Table(ABC):
    """Table abstract class"""

    @abstractmethod
    def get_class_name(self) -> str:
        """
        returns the class name
        :return: str
        """

    @abstractmethod
    def get_primary_key(self) -> str:
        """
        returns the primary key of the database table
        :return: str
        """

    def get_dict(self) -> dict:
        """
        create a data dict of itself
        :return: data dict
        """
        data_dict_self = {}
        attribute_self = self.__dict__
        for name_attribute in attribute_self.keys():
            value = self.__getattribute__(name_attribute)
            if isinstance(value, Enum):
                value = value.value
            elif isinstance(value, date) or isinstance(value, time):
                value = value.__str__()
            data_dict_self[name_attribute] = value
        return data_dict_self
