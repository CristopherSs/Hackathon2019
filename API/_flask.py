"""
    this file contain:
    :ApplicationFlask-> one minimun object based on flask
"""
from typing import Dict

from flask import Flask

from API.resources_api.api import Api


class ApplicationFlask(Flask):
    """
        object based on flask
    """

    def __init__(self) -> None:
        Flask.__init__(self, 'Application Flask')
        self.__resources_with_api = []

    def register_url_of_resource_api(self, resource: Api) -> None:
        """
        this method receive a class type Api for add the class on list
        :param resource: object from methodview
        :return: nothing
        """
        self.__resources_with_api.append(resource)

    def run(self, host: str = None, port: str = None, debug: bool = True,
            load_dotenv: bool = True, **options: Dict) -> None:
        """
        this method iterate the list for do the register url from resource
        :param debug: is for on the flask
        :return: nothing
        """

        for resource in self.__resources_with_api:
            resource.register_url(self)
        Flask.run(self, host=host, port=port, debug=debug)
