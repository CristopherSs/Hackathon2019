import unittest

from backend.emergency_signal import EmergencySignal


class TestEmergencySignal(unittest.TestCase):

    def test_get_departments_ids(self):
        disaster_department = [{'disaster_id': 1, 'department_id': 6},
                               {'disaster_id': 1, 'department_id': 13}]
        emergency = EmergencySignal(disaster_department)
        actual = emergency.get_departments_ids()
        expected = [6, 13]
        self.assertEqual(expected, actual)
