from src.model.classes_model import ClassesModel
from src.model.equipment_model import EquipmentModel
from src.model.manager_model import GymManagerModel
from src.model.member_model import MemberModel
from src.model.staff_model import StaffModel
from src.model.workout_zone_model import WorkoutZoneModel
from typing import Type


class GymModel:

    initial_id = 100

    def __init__(self, city: str, manager: GymManagerModel = None):
        self.__id = GymModel.initial_id
        GymModel.initial_id += 1
        self.__city = city
        self.__manager = manager
        self.__workout_zones = []
        self.__list_of_staff = []
        self.__list_of_members = []
        self.__list_of_classes = []

    def get_gym_id(self) -> int:
        return self.__id

    def get_gym_city(self) -> str:
        return self.__city

    def get_gym_manager(self) -> GymManagerModel:
        return self.__manager

    def get_gym_workout_zones(self) -> list[WorkoutZoneModel]:
        return self.__workout_zones

    def get_equipments_for_workout_zones(self) -> list[EquipmentModel]:
        equipment_list = []
        for workout_zone in self.__workout_zones:
            equipment_list.append(workout_zone.get_list_of_equipments())
        return equipment_list

    def get_list_of_staff(self) -> list[StaffModel]:
        return self.__list_of_staff

    def get_list_of_members(self) -> list[Type[MemberModel]]:
        return self.__list_of_members

    def get_list_of_classes(self) -> list[ClassesModel]:
        return self.__list_of_classes

    def set_gym_city(self, city: str):
        self.__city = city

    def set_gym_manager(self, manager: GymManagerModel):
        self.__manager = manager

    def add_workout_zone(self, workout_zone: WorkoutZoneModel):
        self.__workout_zones.append(workout_zone)

    def add_staff(self, staff: StaffModel):
        self.__list_of_staff.append(staff)

    def add_member(self, member: Type[MemberModel]): # Type[] helps Python accept the use of subclasses
        self.__list_of_members.append(member)

    def add_class(self, gym_class: ClassesModel):
        self.__list_of_classes.append(gym_class)