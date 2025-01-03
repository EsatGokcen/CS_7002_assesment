from src.model.equipment_model import EquipmentModel
from src.model.staff_model import StaffModel


class WorkoutZoneModel:

    def __init__(self, type: str, capacity: int):
        self.__type = type
        self.__capacity = capacity
        self.__list_of_equipments = []
        self.__attendant = None

    def __str__(self):
        return f"{self.__type} with capacity: {self.__capacity}."

    def get_workout_zone_type(self) -> str:
        return self.__type

    def get_workout_zone_capacity(self) -> int:
        return self.__capacity

    def get_list_of_equipments(self) -> list[EquipmentModel]:
        return self.__list_of_equipments

    def get_attendant(self) -> StaffModel:
        return self.__attendant

    def set_type(self, type: str):
        self.__type = type

    def set_capacity(self, capacity: int):
        self.__capacity = capacity

    def set_equipment(self, equipment: EquipmentModel):
        self.__list_of_equipments.append(equipment)

    def set_attendant(self, attendant: StaffModel):
        self.__attendant = attendant


