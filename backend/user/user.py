"""user Module"""
from backend.user.user_model import UserModel
from database.i_table import Table
from dataclasses import dataclass
from backend.user.disability import Disabilities


@dataclass
class User(Table, UserModel):
    name: str
    last_name: str
    gender: str
    disability: Disabilities

    def get_primary_key(self):
        return 'email_id'

    def get_class_name(self) -> str:
        return self.__class__.__name__
