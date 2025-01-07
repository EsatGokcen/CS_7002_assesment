from src.model.classes_model import ClassesModel
from src.model.member_model import MemberModel
from src.model.staff_model import StaffModel
from src.model.workout_zone_model import WorkoutZoneModel
from src.view.classes_view import ClassesView
from typing import Type


class ClassesController:

    def __init__(self):
        self.model = ClassesModel(name="placeholder", date="00/00/00", hour="12:00")
        self.__view = ClassesView(self.model)

    def create_class(self, name: str, date: str, hour: str, capacity: int, teacher: StaffModel, location: WorkoutZoneModel) -> ClassesModel:
        self.model.set_name(name)
        self.model.set_date(date)
        self.model.set_hour(hour)
        self.model.set_location(location)
        self.model.set_capacity(capacity)
        self.model.set_teacher(teacher)
        return self.model

    def add_attendee(self, attendee: Type[MemberModel]) -> Type[MemberModel]:
        self.model.add_attendee(attendee)
        return attendee

    def update_teacher(self, teacher: StaffModel):
        self.model.set_teacher(teacher)

    def read_class(self):
        print(self.__view.render())