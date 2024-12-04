from src.model.equipment_model import EquipmentModel

class WorkoutZoneModel:

    def __init__(self, type: str, capacity: int):
        self.__type = type
        self.__capacity = capacity

    def __str__(self):
        return f"{self.__type} with capacity: {self.__capacity}"

    def get_workout_zone_type(self):
        return self.__type

    def get_workout_zone_capacity(self):
        return self.__capacity

    def set_type(self, type):
        self.__type = type

    def set_capacity(self, capacity):
        self.__capacity = capacity


