from src.model.equipment_model import EquipmentModel
from src.view.equipment_view import EquipmentView


class EquipmentController:

    def __init__(self):
        self.model = EquipmentModel(name="Dumbbell", type="Weight")
        self.__view = EquipmentView(self.model)

    def create_equipment(self, name: str, type: str):
        self.model.set_equipment_name(name)
        self.model.set_equipment_type(type)
        return self.model

    def read_equipment(self):
        print(self.__view.render())