"""Exceptions module"""


class NoConnection(Exception):
    """No Connection exception class"""
    def __init__(self) -> None:
        message = 'There is no connection to a database'
        super(NoConnection, self).__init__(message)

class IsNotATable(Exception):
    """Exception for when a class is not a table"""
    def __init__(self, name: str) -> None:
        message = '{} is not a table type class'.format(name)
        super(IsNotATable, self).__init__(message)
