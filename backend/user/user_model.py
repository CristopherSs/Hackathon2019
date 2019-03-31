"""User module"""
from dataclasses import dataclass


@dataclass
class UserModel:
    """User Interface"""
    email: str
    password: str

    def __eq__(self, other: 'UserModel') -> bool:
        """

        :param other:
        :return:
        """
        if self.email == other.email and self.password == other.password:
            return True
        return False
