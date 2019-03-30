import unittest

from backend.user.disability import Disabilities
from database.logical_operator import LogicalOperator
from database.query_constructor import QueryConstructor
from database.condition import Condition


class TestQueryConstructor(unittest.TestCase):
    def test_save(self):
        constructor = QueryConstructor('rooms')
        room_id = 'D4-02'
        is_available = '1'
        computers = '20'
        column_value = {'room_id': room_id, 'is_available':is_available,
                        'computers':computers}
        actual = constructor.save(column_value)

        expected = 'INSERT INTO rooms (room_id,is_available,computers) VALUES ("D4-02", "1", "20")'
        self.assertEqual(expected, actual)

    def test_save_enum_case(self):
        constructor = QueryConstructor('rooms')
        room_id = 'D4-02'
        disability = Disabilities.NONE
        column_value = {'room_id': room_id, 'data_display_type': disability}
        actual = constructor.save(column_value)
        expected = 'INSERT INTO rooms (room_id,data_display_type) ' \
                   'VALUES ("D4-02", "none")'
        self.assertEqual(expected, actual)

    def test_delete(self):
        constructor = QueryConstructor('user')
        parameter_name = 'user_name'
        value = 'sebas777'
        actual = constructor.delete(parameter_name, value)
        expected = 'DELETE FROM user where user_name="sebas777";'
        self.assertEqual(expected, actual)

    def test_update(self):
        constructor = QueryConstructor('rooms')
        parameter_name = 'room_id'
        value = 'd4-02'
        new_values = {'computers': '50', 'has_whiteboard': '1'}
        actual = constructor.update(parameter_name, value, new_values)

        expected = 'UPDATE rooms SET computers="50",has_whiteboard="1" WHERE room_id="d4-02";'
        self.assertEqual(expected, actual)

    def test_get_all(self):
        constructor = QueryConstructor('rooms')
        actual = constructor.get_all()
        expected = 'SELECT * from rooms'
        self.assertEqual(expected, actual)

    def test_get_one(self):
        constructor = QueryConstructor('rooms')
        condition = Condition('room_id', '=', 'D4-02')
        actual = constructor.get_specific_data([condition])
        expected = 'SELECT * FROM rooms WHERE  room_id = "D4-02" '
        self.assertEqual(expected, actual)

    def test_create_table(self):
        constructor = QueryConstructor('rooms')
        columns = {'room_id': ['varchar(10)', 'PRIMARY KEY'],
                   'capacity': ['int(5)', 'NOT NULL'], 'is_available': ['tinyint(1)', 'NOT NULL']}
        expected = 'CREATE TABLE IF NOT EXISTS rooms (room_id varchar(10) PRIMARY KEY, ' \
                   'capacity int(5) NOT NULL, is_available tinyint(1) NOT NULL)'
        actual = constructor.create_table(columns)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
