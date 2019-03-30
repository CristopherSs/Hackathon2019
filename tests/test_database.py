import unittest

from backend.disaster.disaster import Disaster
from database.condition import Condition
from database.database import Database
from tests.mocks.mock_query_launcher import MockQueryLauncher
from database.exceptions import IsNotATable


class TestDatabase(unittest.TestCase):
    def test_save_data(self):
        disaster_data = {'disaster_name': 'fire', 'department_id': 1}
        disaster = Disaster(**disaster_data)
        query_launcher = MockQueryLauncher(0)
        database = Database(query_launcher)
        actual = database.save_data(disaster)
        self.assertEqual(actual, disaster)

    def test_save_auto_increment_pk_case(self):
        disaster_data = {'disaster_name': 'fire', 'department_id': 1}
        disaster = Disaster(**disaster_data)
        query_launcher = MockQueryLauncher(1)
        database = Database(query_launcher)
        actual = database.save_data(disaster)
        self.assertEqual(actual.disaster_id, 1)

    def test_update(self):
        disaster_data = {'disaster_name': 'fire', 'department_id': 1}
        disaster = Disaster(**disaster_data)
        query_launcher = MockQueryLauncher()
        database = Database(query_launcher)
        actual = database.update(disaster)
        self.assertEqual(disaster, actual)

    def test_update_fail_case(self):
        rooms_list = Exception()
        query_launcher = MockQueryLauncher()
        database = Database(query_launcher)
        with self.assertRaises(IsNotATable) as error:
            database.update(rooms_list)
        expected = 'Exception is not a table type class'
        self.assertEqual(expected, str(error.exception))

    def test_delete(self):
        disaster_data = {'disaster_name': 'fire', 'department_id': 1}
        disaster = Disaster(**disaster_data)
        query_launcher = MockQueryLauncher()
        database = Database(query_launcher)
        actual = database.delete(disaster)
        self.assertTrue(actual)

    def test_get_specific_data(self):
        data = [{'disaster_name': 'fire', 'department_id': 1}, {'disaster_name': 'fire', 'department_id': 2}]
        conditions = [Condition('disaster_name', '=', 'fire')]

        query_launcher = MockQueryLauncher(data)
        database = Database(query_launcher)
        disasters = database.get_specific_data(Disaster, conditions)
        self.assertEqual(Disaster, type(disasters[0]))

    def test_get_specifict_data_launch_returns_a_number_case(self):
        conditions = [Condition('is_free', '=', '1')]
        query_launcher = MockQueryLauncher()
        database = Database(query_launcher)
        disasters = database.get_specific_data(Disaster, conditions)
        expected = []
        self.assertEqual(expected, disasters)

    def test_get_all(self):
        data = [{'disaster_name': 'fire', 'department_id': 1}, {'disaster_name': 'fire', 'department_id': 2}]
        expected = []
        for row in data:
            expected.append(Disaster(**row))
        query_launcher = MockQueryLauncher(data)
        database = Database(query_launcher)
        actual = database.get_all(Disaster)
        self.assertEqual(expected, actual)

    def test_get_all_launch_returns_a_number_case(self):
        query_launcher = MockQueryLauncher()
        database = Database(query_launcher)
        actual = database.get_all(Disaster)
        expected = []
        self.assertEqual(expected, actual)
