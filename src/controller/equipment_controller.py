from src.model.equipment_model import EquipmentModel


class EquipmentController:

    def __init__(self):
        self.__list_of_equipments = []

    def create_equipment(self, name: str, type: str):
        equipment = EquipmentModel(name, type)
        return self.__list_of_equipments.append(equipment)

    def read_equipment(self):
        if not self.__list_of_equipments:
            return "No registered equipments"
        return self.__list_of_equipments