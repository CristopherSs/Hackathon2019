"""query constructor module"""
from enum import Enum
from typing import Dict, List
from database.logical_operator import LogicalOperator

from Rooms.database.condition import Condition


class QueryConstructor:
    """Query Constructor class"""

    def __init__(self, table_name: str) -> None:
        self.__table_name = table_name

    def save(self, column_value: Dict) -> str:
        """
        constructs the query for saving data on any table
        :param table_name: str
        :param column_value: dict
        :return: bool
        """
        columns = list(column_value.keys())
        values = column_value.values()
        columns_names = ','.join(columns)
        variable_on_list = []
        for item in values:
            if isinstance(item, Enum):
                item = item.value
            variable_on_list.append('"' + str(item) + '"')
        rows = (', '.join(variable_on_list))
        query = 'INSERT INTO {0} ({1}) VALUES ({2})'. \
            format(self.__table_name, columns_names, rows)
        return query

    def delete(self, parameter_name: str, value: str) -> str:
        """
        constructs query to delete a row from a table
        :param table_name: str
        :param parameter_name: str
        :param value: str
        :return: bool
        """
        query = 'DELETE FROM {0} where {1}="{2}";'. \
            format(self.__table_name, parameter_name, value)
        return query

    def update(self, parameter_name: str, value: str,
               new_values: Dict[str, str]) -> str:
        """
        constructs query to update a row from the table
        :param table_name: str
        :param parameter_name: str
        :param value: str
        :param new_values: str
        :return: str
        """
        keys = new_values.keys()
        values = new_values.values()
        mixed_list = ','. \
            join([key + '=' + '"' + str(value) + '"' for key, value in zip(keys, values)])
        query = 'UPDATE {0} SET {1} WHERE {2}="{3}";'. \
            format(self.__table_name, mixed_list, parameter_name, value)

        return query

    def get_all(self) -> str:
        """
        constructs query to get the values in a table
        :param table_name: str
        :return: str
        """
        query = 'SELECT * from {0}'.format(self.__table_name)
        return query

    def get_specific_data(self, conditions: List[Condition],
                          logical_operator: LogicalOperator = LogicalOperator.AND) -> str:
        """
        constructs query to get one row of the table
        :param conditions: List[Condition]
        :param logical_operator: Enum
        :return: str
        """

        all_conditions = logical_operator.value. \
            join(' ' + condition.build_condition() + ' ' for condition in conditions)
        query = 'SELECT * FROM {0} WHERE {1}'. \
            format(self.__table_name, all_conditions)
        return query

    def create_table(self, columns_dict: Dict, constraints: List = None) -> str:
        """
        constructs the query to create a table
        :param columns_dict: Dict
        :param constraints: List
        :return: str
        """
        if not constraints:
            constraints = []
        column = columns_dict.keys()
        column_type = columns_dict.values()
        columns = ', '. \
            join(column_name + ' ' + ' '.join(column_type)
                 for column_name, column_type in zip(column, column_type))
        query = 'CREATE TABLE IF NOT EXISTS {0} ({1}'.format(self.__table_name, columns)
        if constraints:
            constructed_constraints = ', '.join(constraint for constraint in constraints)
            query = query + ', ' + constructed_constraints
        query = query + ')'
        return query
