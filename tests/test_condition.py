import unittest

from database.condition import Condition


class TestCondition(unittest.TestCase):

    def test_build_condition(self):
        condition = Condition('room_id', '=', 'D4-02')
        actual = condition.build_condition()
        expected = 'room_id = "D4-02"'
        self.assertEqual(expected, actual)

    def test_get_parameter_name(self):
        condition = Condition('room_id', '=', 'D4-02')
        actual = condition.get_parameter_name()
        expected = 'room_id'
        self.assertEqual(expected, actual)

    def test_get_operand(self):
        condition = Condition('room_id', '=', 'D4-02')
        actual = condition.get_operand()
        expected = '='
        self.assertEqual(expected, actual)

    def test_get_value(self):
        condition = Condition('room_id', '=', 'D4-02')
        actual = condition.get_value()
        expected = 'D4-02'
        self.assertEqual(expected, actual)