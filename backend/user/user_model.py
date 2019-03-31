"""User module"""
from dataclasses import dataclass


@dataclass
class UserModel:
    """User Interface"""
    email_id: str
    password: str

    def __eq__(self, other: 'UserModel') -> bool:
        """

        :param other:
        :return:
        """
        if self.email_id == other.email_id and self.password == other.password:
            return True
        return False
