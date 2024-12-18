
class EquipmentModel:

    def __init__(self, name: str, type: str):
        self.__name = name
        self.__type = type

    def __str__(self):
        return f"{self.__name} for {self.__type}"

    def get_equipment_name(self) -> str:
        return self.__name

    def get_equipment_type(self) -> str:
        return self.__type

    def set_equipment_name(self, name):
        self.__name = name

    def set_equipment_type(self, type):
        self.__type = type

