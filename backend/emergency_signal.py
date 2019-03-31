from typing import List, Dict


class EmergencySignal:
    def __init__(self, disaster_departments: List) -> None:
        self.__disaster_departments = disaster_departments

    def get_departments_ids(self) -> List:
        """

        :return:
        """
        departments_id = list()
        for disaster_department in self.__disaster_departments:
            departments_id.append(disaster_department['department_id'])
        return departments_id
