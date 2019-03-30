"""mock Cursor module"""
from typing import Union


class MockCursor:
    """MockCursor class"""
    def __init__(self, fetchall_return_value: Union[list, Exception] = None,
                 execute_return_value: Exception = None,
                 column_names: tuple = None,
                 lastrowid: int = 0) -> None:
        self.__execute_return_value = execute_return_value
        self.__fetchall_return_value = fetchall_return_value
        self.column_names = column_names
        self.lastrowid = lastrowid

    def execute(self, sql_query: str) -> None:
        if self.__execute_return_value:
            raise Exception('error: ' + sql_query)
        return self.__execute_return_value

    def fetchall(self) -> Union[None, list]:
        if type(self.__fetchall_return_value) is Exception:
            raise Exception()
        return self.__fetchall_return_value