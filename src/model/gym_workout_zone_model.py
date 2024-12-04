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

    def get_equipment(self):
        equipments = ", ".join(str(equipment) for equipment in self.__list_of_equipments)
        return f"{equipments}"

    def set_type(self, type: str):
        self.__type = type

    def set_capacity(self, capacity: int):
        self.__capacity = capacity

    def set_equipment(self, equipment: EquipmentModel):
        self.__list_of_equipments.append(equipment)


