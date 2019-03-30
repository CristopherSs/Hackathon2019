"""Table generator module"""
from Rooms.database.i_query_launcher import IQueryLauncher
from Rooms.database.i_table import Table
from Rooms.database.query_constructor import QueryConstructor
from Rooms.database.table_generator.class_decomposer import ClassDecomposer


class TableGenerator: # pylint: disable=too-few-public-methods
    """TableGenerator class"""
    def __init__(self, query_launcher: IQueryLauncher) -> None:
        self.__launcher = query_launcher

    def generate(self, instance: Table, pk_auto_increment: bool = False) -> str:
        """
        generates a table from an instance
        :param instance: instance of a Table object
        :param pk_auto_increment: bool
        :return: None
        """
        query_constructor = QueryConstructor(instance.get_class_name())
        decomposer = ClassDecomposer(instance, pk_auto_increment)
        data = decomposer.decompose()
        if data[1]:
            query = query_constructor.create_table(data[0], data[1])
        else:
            query = query_constructor.create_table(data[0])
        self.__launcher.launch(query)
        return query
