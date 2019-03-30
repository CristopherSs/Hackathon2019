"""this file contains an interface of query launcher"""
from abc import ABC, abstractmethod
from typing import Union, List, Dict

class IQueryLauncher(ABC): # pylint: disable=too-few-public-methods
    """InterfaceQueryLauncher class"""
    @abstractmethod
    def launch(self, sql_query: str, fetch: bool = False) -> Union[int, List[Dict]]:
        """
        abstract method for launch
        :param sql_query: str
        :param fetch: bool
        :return: None or List
        """
