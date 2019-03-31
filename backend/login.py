from typing import List


class LoginVerifier:
    """Login Verifier for when someone tries to login"""
    def __init__(self, existent_users: List) -> None:
        self.__existent_users = existent_users

    def login(self, email: str, password: str) -> bool:
        """
        compares email and password in case the email exists in the database
        :param email: str
        :param password: str
        :return: bool
        """
        for user_data in self.__existent_users:
            if user_data['email'] == email:
                if user_data['password'] == password:
                    return True
                else:
                    return False
        return False
