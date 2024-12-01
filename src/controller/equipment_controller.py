from src.model.equipment_model import EquipmentModel
from src.view.equipment_view import EquipmentView


class EquipmentController:

    def __init__(self):
        self.__model = EquipmentModel(name="Dumbbell", type="Weight")
        self.__view = EquipmentView(self.__model)

    def create_equipment(self, name: str, type: str):
        self.__model.set_equipment_name(name)
        self.__model.set_equipment_type(type)

    def read_equipment(self):
        return self.__view.render()