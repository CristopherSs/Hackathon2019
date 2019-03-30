"""condition module"""


class Condition:
    """condition Class"""

    def __init__(self, parameter_name: str, operand: str, value: str) -> None:
        self.__parameter_name = parameter_name
        self.__operand = operand
        self.__value = value

    def build_condition(self) -> str:
        """

        :return:
        """
        condition = '{0} {1} "{2}"'.format(self.__parameter_name, self.__operand,
                                           self.__value)
        return condition

    def get_parameter_name(self) -> str:
        """

        :return:
        """
        return self.__parameter_name

    def get_operand(self) -> str:
        """

        :return:
        """
        return self.__operand

    def get_value(self) -> str:
        """

        :return:
        """
        return self.__value

    def set_value(self, new_value: str) -> None:
        """
        change value
        :param new_value: new value to examine
        :return: None
        """
        self.__value = new_value
