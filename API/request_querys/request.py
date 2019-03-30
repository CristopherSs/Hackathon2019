"""this file contain:
    Query:this class is one test for use API
"""
from copy import copy
from typing import Union
from datetime import date

import requests

from Rooms.backend.room.room import Room
from Rooms.backend.booking.only_booking import Booking
from Rooms.backend.user.user import User


class Query:
    """
        this class do all operation of query necesary with CRUD on Database

    """

    def __init__(self, data_url: dict) -> None:
        self.__reference = data_url['reference']
        _ip = data_url['ip']
        port = data_url['port']
        name_table = self.__reference.__name__
        self.__url = 'http://{0}:{1}/{2}/'.format(_ip, port, name_table)

    def save_data(self, save_data: Union[Room, Booking]) -> object:
        """
        this method save to object
        :param upgrade:
        :return: object
        """
        if self.__verify_type_send_exception(type(save_data)):
            request = requests.post(self.__url, json=save_data.get_dict())
            if request.status_code != 200:
                raise ValueError(str(save_data))
            data_saved = request.json()[0]
        return copy(self.__reference(**data_saved))

    def upgrade_data(self, upgrade_data: Union[Room, Booking]) -> object:
        """
        this method upgrade all data from object on database
        :return:object
        """
        if self.__verify_type_send_exception(type(upgrade_data)):
            data_saved = requests.put(self.__url, json=upgrade_data.get_dict()).json()[0]
        return copy(self.__reference(**data_saved))

    def delete_data(self, delete_data: Union[Room, Booking, User]) -> None:
        """
            this method delete to object

        :param delete_data: object to delete
        :return: nothing
        """
        if self.__verify_type_send_exception(type(delete_data)):
            data_on_dict = delete_data.get_dict()
            requests.delete(self.__url + data_on_dict[delete_data.get_primary_key()],
                            json=data_on_dict)

    def get_data(self, _id: str = '') -> object:
        """
        this method obtain all data from primary key and insert any type for managers
        :return: RoomsList or Bookings
        """
        data_table = requests.get(self.__url + _id).json()
        list_with_objects = []  # type:list
        for data in data_table:
            list_with_objects.append(data)
        return list_with_objects

    def __verify_type_send_exception(self, instance_verify: type) -> bool:
        """
        verify if the parametrer is equal type
        :param instance: type instance to verify
        :return: true if is equal
        """
        if self.__reference is instance_verify:
            return True
        raise Exception("uncorrect type")

    def get_specific_data(self, data_name: str, operator: str, value: str = None):
        """
        this method obtain all data from the reference
        where data is value using the operator
        :param data_name: name of column in database
        :param operator: operator
        :param value: value to compare
        :return: List of dicts
        """
        request = requests.get(self.__url + '/' + data_name + '/' + operator + '/' + value)
        return list(request.json())

    def get_of_date(self, room_id: str, object_date: date):
        """
                this method obtain all data from the reference
                where data is value using the operator
                :param room_id: name of room in database
                :param object_date: searched date
                :return: List of dicts
                """
        url = self.__url + room_id + '/' + object_date.strftime('%Y-%m-%d')
        request = requests.get(url)
        return list(request.json())
