"""Class decomposer module"""
from datetime import date, time
from enum import Enum
from database.i_table import Table
from database.exceptions import IsNotATable


class ClassDecomposer:
    """Decompose a class"""

    def __init__(self, instance: Table, pk_auto_increment: bool = False) -> None:
        self.__instance = instance
        self.__auto_increment = pk_auto_increment

    def identify_variable_type(self, variable_name: str) -> tuple:
        """
        identifies all variable type
        :param variable_name: str
        :return: tuple
        """
        variables_type = list()
        constraint = None
        attribute = self.__instance.__getattribute__(variable_name)
        variable_type = type(attribute)
        if isinstance(attribute, Table):
            variable_type = type(attribute.__getattribute__(attribute.get_primary_key()))
        if isinstance(attribute, Enum):
            variable_type = type(attribute.value)
        if variable_type is int and ('has' != variable_name[0:3] != 'is_'):
            variables_type.append('INT(5)')
        elif variable_type is str:
            variables_type.append('VARCHAR(50)')
        elif variable_name[0:3] == 'is_' or variable_name[0:3] == 'has':
            variables_type.append('TINYINT(1)')
        elif variable_type is date:
            variables_type.append('DATE')
        elif variable_type is time:
            variables_type.append('TIME')

        if variable_name == self.__instance.get_primary_key():
            variables_type.append('PRIMARY KEY')
            if self.__auto_increment:
                variables_type.append('AUTO_INCREMENT')
        if variable_name[len(variable_name) - 3: len(variable_name)] == '_id' and \
                variable_name != self.__instance.get_primary_key():
            table_name = (variable_name[0: len(variable_name) - 3]).capitalize()
            constraint = 'CONSTRAINT FOREIGN KEY ({0}) ' \
                         'REFERENCES {1}({0}) ON DELETE ' \
                         'CASCADE ON UPDATE RESTRICT'.format(variable_name, table_name)
        variables_type.append('NOT NULL')
        return variables_type, constraint

    def decompose(self) -> tuple:
        """
        decompose a class getting all variable names, types and values
        :return: Dict
        """
        if isinstance(self.__instance, Table):
            constraints = []
            columns_name_and_type = dict()
            class_variables = self.__instance.get_dict()
            variables_names = class_variables.keys()
            for variable_name in variables_names:
                variables_type = self.identify_variable_type(variable_name)
                columns_name_and_type[variable_name] = variables_type[0]
                if variables_type[1]:
                    constraints.append(variables_type[1])
            return columns_name_and_type, constraints
        raise IsNotATable(self.__instance.__class__.__name__)
