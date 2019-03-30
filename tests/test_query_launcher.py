import unittest
from unittest.mock import MagicMock, patch
from database.exceptions import NoConnection
from database.query_launcher import QueryLauncher
from tests.mocks.mock_cursor import MockCursor
from tests.mocks.mock_connection import MockConnection


class TestQueryLauncher(unittest.TestCase):

    @patch('database.query_launcher.mariadb')
    def test_launch_fail_case(self, mock):
        mocked_connection = MockConnection()
        mock.connect.return_value = mocked_connection
        config = {'user': '', 'password': '', 'database': '', 'host': ''}
        query_launcher = QueryLauncher(config)
        with self.assertRaises(NoConnection) as error:
            query_launcher.launch('query')
        expected = 'There is no connection to a database'
        self.assertEqual(expected, str(error.exception))

    @patch('database.query_launcher.mariadb')
    def test_launch_query_execute_fail_case(self, mock):
        mocked_cursor = MockCursor(execute_return_value=Exception())
        mocked_connection = MockConnection(cursor_return_value=mocked_cursor)
        mock.connect.return_value = mocked_connection
        config = {'user': '', 'password': '', 'database': '', 'host': ''}
        query_launcher = QueryLauncher(config)
        with self.assertRaises(Exception) as error:
            query_launcher.launch('query')
        expected = 'error: query'
        self.assertEqual(expected, str(error.exception))

    @patch('database.query_launcher.mariadb')
    def test_launch_query_save_insert_update_case(self, mock):
        mocked_cursor = MockCursor(fetchall_return_value=Exception(), lastrowid=5)
        mocked_connection = MockConnection(cursor_return_value=mocked_cursor)
        mock.connect.return_value = mocked_connection
        config = {'user': '', 'password': '', 'database': '', 'host': ''}
        query_launcher = QueryLauncher(config)
        actual = query_launcher.launch('query')
        expected = 5
        self.assertEqual(expected, actual)

    @patch('database.query_launcher.mariadb')
    def test_launch_query_get_case(self, mock):
        column_names = ('room_id', 'has_whiteboard', 'is_available', 'is_free')
        rows = [('D4-02', 1, 0, 1)]
        mocked_cursor = MockCursor(fetchall_return_value=rows, column_names=column_names)
        mocked_connection = MockConnection(cursor_return_value=mocked_cursor)
        mock.connect.return_value = mocked_connection
        config = {'user': '', 'password': '', 'database': '', 'host': ''}
        query_launcher = QueryLauncher(config)
        actual = query_launcher.launch('query', fetch=True)
        expected = [{'room_id': 'D4-02', 'has_whiteboard': 1, 'is_available': 0, 'is_free': 1}]
        self.assertEqual(expected, actual)

    @patch('database.query_launcher.mariadb')
    def test_change_config_values(self, mock):
        column_names = ('room_id', 'has_whiteboard', 'is_available', 'is_free')
        rows = [('D4-02', 1, 0, 1)]
        mocked_cursor = MockCursor(fetchall_return_value=rows, column_names=column_names)
        mocked_connection = MockConnection(cursor_return_value=mocked_cursor)
        mock.connect.return_value = mocked_connection
        config1 = {'user': '', 'password': '', 'database': '', 'host': ''}
        query_launcher1 = QueryLauncher(config1)
        config2 = {'user': 'user', 'password': 'password', 'database': 'database', 'host': 'host'}
        query_launcher2 = QueryLauncher(config2)

        query_launcher1.change_config_values(config2)
        self.assertTrue(query_launcher1==query_launcher2)


if __name__ == '__main__':
    unittest.main()
