"""
    this file contain the next class:
    Api->interface for diferents views with api
"""
from typing import List
import flask.views as fl
from flask import Flask, request, Response, jsonify

from Rooms.backend.booking.only_booking import Booking
from Rooms.backend.i_verifier import IVerifier
from Rooms.database.condition import Condition
from Rooms.database.database import Database
from Rooms.database.i_table import Table


class Api(fl.MethodView):
    """
        this class is a dataclass with form of superclass
    """

    def __init__(self, reference: type, database: Database,
                 headers: dict, verifier: IVerifier = None) -> None:
        self._database = database
        self.__reference = reference
        self.__reference_name = reference.__name__.lower()
        self.__verifier = verifier
        self.__response_headers = headers

    def post(self) -> jsonify:
        """
        this method insert on database and verifier that not exist on database
        :return: nothing
        """
        data = request.get_json()
        object_from_data = self.__reference(**data)
        method_database = self._database.save_data
        if self.__verifier is None:
            response = self.__execute_method(object_from_data, method_database)
        else:
            response = self.__execute_method(object_from_data, method_database,
                                             self.__verifier.can_add)
        return response

    def put(self) -> jsonify:
        """
        this method update on database
        :return: nothing
        """
        data = request.get_json()
        object_from_data = self.__reference(**data)
        method_database = self._database.update
        if self.__verifier is None:
            response = self.__execute_method(object_from_data, method_database)
        else:
            response = self.__execute_method(object_from_data, method_database,
                                             self.__verifier.can_update)
        return response

    def get(self, _id: str = None) -> jsonify:
        """
        this method dispatch data to  corresponding
        :param id_room: identifier from room
        :return: a list with all data of reference
        """
        if not _id and self.__reference is not Booking:
            list_of_data = self._database.get_all(self.__reference)
        else:
            list_of_data = self._database.get_specific_data \
                (self.__reference, [Condition(self.__reference_name + '_id', '=', _id)])
        return self.__response_jsonify_with_access(list_of_data)

    def delete(self, _id: str) -> jsonify:
        """
        this method delete one object in special
        :return: nothing
        """
        data = request.get_json()
        data[self.__reference_name + '_id'] = _id
        new_objetc = self.__reference(**data)
        self._database.delete(new_objetc)
        return self.__response_jsonify_with_access([new_objetc])

    def options(self, _id: str = None) -> Response:
        """
            this a intemedier for POST,PUT,DELETE
        :return: Response
        """

        return Response(headers=self.__response_headers)

    def register_url(self, app: Flask) -> None:
        """
            this  method write and save url for call on querys with request
         :param app: object type Flask for save the url
        :return: nothing
        """
        fuction = self.as_view('Api' + self.__reference.__name__, self.__reference, self._database,
                               self.__response_headers, self.__verifier)
        app.add_url_rule('/' + self.__reference.__name__ + '/'
                         , view_func=fuction, methods=['GET', 'POST', 'PUT', 'OPTIONS'])
        app.add_url_rule('/' + self.__reference.__name__ +
                         '/<string:_id>', view_func=fuction, methods=['GET', 'DELETE', 'OPTIONS'])

    def __response_jsonify_with_access(self, list_object: list, number_error: int = 200) -> jsonify:

        """this method give access to response Jsonify
            :return Response
        """
        response_json = jsonify(self.__obtain_dictionary_for_json(list_object))
        response_json.headers.add('Access-Control-Allow-Origin', '*')
        response_json.status_code = number_error
        return response_json

    def __obtain_dictionary_for_json(self, list_of_object: list) -> List:
        """
        convert data object on dictionarys
        :return: a list of dictionarys

        """
        list_dictionarys = []
        for instance in list_of_object:
            if self.__reference is type(instance):
                list_dictionarys.append(instance.get_dict())
        return list_dictionarys

    def __execute_method(self, object_to_examine: Table, method_database: type,
                         method_verifier: type = True) -> Response:
        """
            execute the next algorithm
        :param method_database: this method can be save or update any more
        :param method_verifier: this method can be can_add or can_update any more
        :param object_to_examine: a object to save or update
        :return: response with status
        """
        if method_verifier:
            method_database(object_to_examine)
            response = self.__response_jsonify_with_access([object_to_examine])
        else:
            if method_verifier(object_to_examine):
                method_database(object_to_examine)
                response = self.__response_jsonify_with_access([object_to_examine])
            else:
                response = self.__response_jsonify_with_access([object_to_examine], 400)
        return response
