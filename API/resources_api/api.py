"""
    this file contain the next class:
    Api->interface for diferents views with api
"""
from typing import List
import flask.views as fl
from flask import Flask, request, Response, jsonify

from database.condition import Condition
from database.database import Database


class Api(fl.MethodView):
    """
        this class is a dataclass with form of superclass
    """

    def __init__(self, reference: type, database: Database,
                 headers: dict) -> None:
        self._database = database
        self.__reference = reference
        self.__reference_name = reference.__name__.lower()
        self.__response_headers = headers

    def post(self) -> jsonify:
        """
        this method insert on database and verifier that not exist on database
        """
        data = request.get_json()
        object_from_data = self.__reference(**data)
        data_on_object = self._database.save_data(object_from_data)
        return self.__response_jsonify_with_access(self.__obtain_dictionary_for_json([data_on_object]))

    def put(self) -> jsonify:
        """
        this method update on database
        :return: nothing
        """
        data = request.get_json()
        object_from_data = self.__reference(**data)
        data_on_onject = self._database.update(object_from_data)
        return self.__response_jsonify_with_access(self.__obtain_dictionary_for_json([data_on_onject]))

    def get(self) -> jsonify:
        """
        this method dispatch data to  corresponding
        :param id_room: identifier from room
        :return: a list with all data of reference
        """
        if request.args:
            conditions = dict(request.args.to_dict())
            values_database = self._database.get_specific_data \
                (self.__reference, self.__generate_condition(conditions))
            if len(values_database) is 0:
                response = self.__response_jsonify_with_access([], 400)
            else:
                response = self.__response_jsonify_with_access(values_database)
        else:
            list_of_data = self._database.get_all(self.__reference)
            response = self.__response_jsonify_with_access(list_of_data)
        return response

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
                               self.__response_headers)
        app.add_url_rule('/' + self.__reference.__name__ + '/'
                         , view_func=fuction, methods=['GET', 'POST', 'PUT', 'OPTIONS'])

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

    def __generate_condition(self, data_dict: dict) -> list:
        """

        :param data_dict:
        :return:
        """
        conditions = []
        for key in data_dict.keys():
            condition = Condition(key, '=', data_dict[key])
            conditions.append(condition)
        return conditions
