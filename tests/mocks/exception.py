"""exception for mock module"""


class WrongQuery(Exception):
    """Wrong query exception"""
    def __init__(self, msg: str) -> None:
        message = 'Error: {} is not valid'.format(msg)
        super(WrongQuery, self).__init__(message)