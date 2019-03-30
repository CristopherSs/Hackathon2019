""""Disaster module"""
from dataclasses import dataclass
<<<<<<< HEAD

from API.request_querys.request import Query
from backend.department.department import Department
=======
>>>>>>> fd31059c66474594e004acae956e574f45e9a8fe
from database.i_table import Table


@dataclass
class Disaster(Table):
    disaster_name: str
    department_id: int
    disaster_id: int = 0

    def get_primary_key(self) -> str:
        return 'disaster_id'

    def get_class_name(self) -> str:
        return self.__class__.__name__

    def contact_department(self) -> None:
        data = {'reference': Department, 'ip': '', 'port': '8080'}
        request = Query(data)
        department = request.get_data(str(self.disaster_id))
