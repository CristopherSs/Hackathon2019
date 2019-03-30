"""Server module"""
from typing import Union, Dict, List
import mysql.connector as mariadb
from database.exceptions import NoConnection
from database.i_query_launcher import IQueryLauncher


class QueryLauncher(IQueryLauncher):
    """Query Launcher class"""

    def __init__(self, config: Dict) -> None:
        self.__user = config['user']
        self.__password = config['password']
        self.__database = config['database']
        self.__host = config['host']

    def change_config_values(self, config: Dict) -> None:
        """
        changes the value of config dict
        :param config: Dict
        :return: None
        """
        self.__user = config['user']
        self.__password = config['password']
        self.__database = config['database']
        self.__host = config['host']

    def __connect(self) -> tuple:
        """
        connects to the database,
        should be private but is public for mocking it with MagicMock
        :return: None
        """
        connection = mariadb.connect(
            user=self.__user,
            passwd=self.__password,
            database=self.__database,
            host=self.__host)
        cursor = connection.cursor()
        return connection, cursor

    def launch(self, sql_query: str, fetch: bool = False) -> Union[int, List[Dict]]:
        """
        launch any query
        :param sql_query: str
        :param fetch: bool
        :return: None
        """
        connection, cursor = self.__connect()
        if cursor:
            cursor.execute(sql_query)
        else:
            raise NoConnection()
        if fetch:
            rows_dict: List[Dict] = list()
            rows_tuples = cursor.fetchall()
            for row in rows_tuples:
                rows_dict.append(dict(zip(cursor.column_names, row)))
        else:
            connection.commit()
            return cursor.lastrowid
        return rows_dict

    # pylint: disable=W0212
    def __eq__(self, query_launcher: object) -> bool:
        """
        compares two query launchers
        :param query_launcher: IQueryLauncher
        :return: bool
        """
        if isinstance(query_launcher, QueryLauncher):
            if (self.__user == query_launcher.__user and
                    self.__password == query_launcher.__password and
                    self.__host == query_launcher.__host and
                    self.__database == query_launcher.__database):
                return True
            return False
        return False
