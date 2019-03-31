"""user Module"""
from enum import Enum

from backend.user.user_model import UserModel
from backend.user.user_state import UserState
from database.i_table import Table
from dataclasses import dataclass
from backend.user.disability import Disabilities


@dataclass
class User(Table, UserModel):
    name: str
    last_name: str
    gender: str
    disability: Disabilities
    user_state: Enum = UserState.SAVE
    user_id: int = 0

    def get_primary_key(self):
        return 'user_id'

    def get_class_name(self) -> str:
        return self.__class__.__name__
