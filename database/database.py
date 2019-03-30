"""database module"""
from typing import List
from Rooms.database.i_query_launcher import IQueryLauncher
from Rooms.database.logical_operator import LogicalOperator
from Rooms.database.query_constructor import QueryConstructor
from Rooms.database.i_table import Table
from Rooms.database.exceptions import IsNotATable


class Database:
    """Database class"""

    def __init__(self, query_launcher: IQueryLauncher) -> None:
        self.__query_launcher = query_launcher

    def save_data(self, instance: Table) -> Table:
        """
        saves all variable values in a table
        :param instance: object
        :table_name: str
        :return: None
        """
        if isinstance(instance, Table):
            table_name = instance.get_class_name()
            query_constructor = QueryConstructor(table_name)
            class_variables = instance.get_dict()
            query = query_constructor.save(class_variables)
            pk_id = self.__query_launcher.launch(query)
            if pk_id:
                instance.__setattr__(instance.get_primary_key(), pk_id)
                return instance
            return instance
        raise IsNotATable(instance.__class__.__name__)

    def update(self, instance: Table) -> Table:
        """
        updates a row in a table
        :param instance: Object
        :return: None
        """
        if isinstance(instance, Table):
            table_name = instance.get_class_name()
            primary_key_name = instance.get_primary_key()
            query_constructor = QueryConstructor(table_name)
            class_variables = instance.get_dict()
            query = query_constructor.update(primary_key_name,
                                             instance.__getattribute__(primary_key_name),
                                             class_variables)
            self.__query_launcher.launch(query)
            return instance
        raise IsNotATable(instance.__class__.__name__)

    def delete(self, instance: Table) -> bool:
        """
        deletes a row in a table
        :param instance: Table
        :return: None
        """
        if isinstance(instance, Table):
            table_name = instance.get_class_name()
            primary_key_name = instance.get_primary_key()
            query_constructor = QueryConstructor(table_name)
            query = query_constructor.delete(primary_key_name,
                                             instance.__getattribute__(primary_key_name))
            self.__query_launcher.launch(query)
            return True
        raise IsNotATable(instance.__class__.__name__)

    def get_specific_data(self, obj_type: type, conditions: List,
                          logical_operator: LogicalOperator = LogicalOperator.AND) -> List:
        """
        gets specific data of any table
        :param obj_type: type
        :param conditions: List[Condition]
        :param logical_operator: LogicalOperator(Enum)
        :return: Table
        """
        objects = []
        query_constructor = QueryConstructor(obj_type.__name__)
        query = query_constructor.get_specific_data(conditions, logical_operator)
        data = self.__query_launcher.launch(query, True)
        if isinstance(data, list):
            for row in data:
                instance = obj_type(**row)
                objects.append(instance)
        return objects

    def get_all(self, obj_type: type) -> List:
        """

        :param obj_type:
        :return:
        """
        list_of_objects = []
        query_constructor = QueryConstructor(obj_type.__name__)
        query = query_constructor.get_all()
        data = self.__query_launcher.launch(query, True)
        if isinstance(data, list):
            for row in data:
                list_of_objects.append(obj_type(**row))
        return list_of_objects
