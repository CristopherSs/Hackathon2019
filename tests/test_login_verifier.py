import unittest

from backend.login import LoginVerifier


class TestLoginVerifier(unittest.TestCase):
    def test_login_success_case(self):
        existent_users = [{'email': 'sebas@hotmail.com', 'password': '1234', 'name': '', 'last_name': ''}]
        login = LoginVerifier(existent_users)
        actual = login.login('sebas@hotmail.com', '1234')
        self.assertTrue(actual)

    def test_login_wrong_password_case(self):
        existent_users = [{'email': 'sebas@hotmail.com', 'password': '1234', 'name': '', 'last_name': ''}]
        login = LoginVerifier(existent_users)
        actual = login.login('sebas@hotmail.com', '4321')
        self.assertFalse(actual)

    def test_login_no_account_case(self):
        existent_users = [{'email': 'sebas@hotmail.com', 'password': '1234', 'name': '', 'last_name': ''}]
        login = LoginVerifier(existent_users)
        actual = login.login('marc@hotmail.com', '1234')
        self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()
