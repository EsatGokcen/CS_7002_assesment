from src.model.member_model import MemberModel
from src.model.staff_model import StaffModel
from src.model.workout_zone_model import WorkoutZoneModel
from typing import Type


class ClassesModel:

    def __init__(self, name: str, date: str):
        self.__name = name
        self.__date = date
        self.__location = None #: WorkoutZoneModel
        self.__capacity = None # < WorkoutZoneModel.get_capacity()
        self.__teacher = None #: StaffModel
        self.__attendees = [] #: list[Type[MemberModel]]

    def __str__(self):
        attendees = ", ".join(str(attendee) for attendee in self.__attendees)
        return (
            f"{self.__name}"
            f"\nClass Date: {self.__date}, Location: {self.__location}"
            f"\nTeacher: {self.__teacher}, Capacity: {self.__capacity}"
            f"\nAttendees:{attendees}"
        )

    def get_name(self) -> str:
        return self.__name

    def get_date(self) -> str:
        return self.__date

    def get_location(self) -> WorkoutZoneModel:
        return self.__location

    def get_capacity(self) -> int:
        return self.__capacity

    def get_teacher(self) -> StaffModel:
        return self.__teacher

    def get_attendees(self) -> list[Type[MemberModel]]:
        return self.__attendees

    def set_name(self, name: str):
        self.__name = name

    def set_date(self, date: str):
        self.__date = date

    def set_location(self, location: WorkoutZoneModel):
        self.__location = location

    def set_capacity(self, capacity: int) -> str:
        if capacity <= self.__location.get_workout_zone_capacity():
            self.__capacity = capacity
            return "Capacity set successfully!"
        elif capacity > self.__location.get_workout_zone_capacity():
            return "Capacity demand too large for location!"
        else:
            raise ValueError("Invalid input!")

    def set_teacher(self, teacher: StaffModel) -> str:
        if teacher == self.__location.get_attendant():
            self.__teacher = teacher
            return "Teacher set successfully!"
        else:
            return "Teacher is not registered!"

    def add_attendee(self, attendee: Type[MemberModel]):
        self.__attendees.append(attendee)
