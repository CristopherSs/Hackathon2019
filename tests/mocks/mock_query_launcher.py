"""Mock query launcher module"""
from database.i_query_launcher import IQueryLauncher
from typing import Union, List, Dict


class MockQueryLauncher(IQueryLauncher):
    """Mock Query Launcher class"""
    def __init__(self, return_value: Union[List[Dict], int] = 0):
        self.__return_value = return_value

    def launch(self, sql_query: str, commit: bool = True) -> Union[None, List[Dict]]:
        return self.__return_value
