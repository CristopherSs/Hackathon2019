"""mock connection Module"""
from tests.mocks.mock_cursor import MockCursor


class MockConnection:
    """Mock Connection class"""
    def __init__(self, commit_return_value=None,
                 cursor_return_value=None) -> None:
        self.__commit_return_value = commit_return_value
        self.__cursor_return_value = cursor_return_value

    def commit(self) -> None:
        return self.__commit_return_value

    def cursor(self):
        return self.__cursor_return_value
