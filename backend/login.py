from flask import request

from API.request_querys.request import Query


class LoginVerifier:
    def __init__(self, api: Query) -> None:
        self.__api = api

    def login(self) -> bool:
        data_to_examine = request.get_json()
        self.__api.get_data(data_to_examine['email_id'])
