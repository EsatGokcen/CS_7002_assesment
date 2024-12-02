from src.model.equipment_model import EquipmentModel

class WorkoutZoneModel:

    def __init__(self, type: str, capacity: int):
        self.__type = type
        self.__capacity = capacity
        self.__list_of_equipments = []

    def __str__(self):
        return f"{self.__type} with capacity: {self.__capacity}"

    def get_workout_zone_type(self):
        return self.__type

    def get_workout_zone_capacity(self):
        return self.__capacity

    def get_list_of_equipments(self):
        return self.__list_of_equipments

    def set_type(self, type):
        self.__type = type

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def add_equipment(self, equipment: EquipmentModel):
        return self.__list_of_equipments.append(equipment)

