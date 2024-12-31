from src.model.equipment_model import EquipmentModel
from src.view.equipment_view import EquipmentView


class EquipmentController:

    def __init__(self):
        self.model = EquipmentModel(name="palceholder", type="placeholder")
        self.__view = EquipmentView(self.model)

    def __str__(self):
        return f"{self.model.get_equipment_name()} for {self.model.get_equipment_type()}"

    def create_equipment(self, name: str, type: str) -> EquipmentModel:
        self.model.set_equipment_name(name)
        self.model.set_equipment_type(type)
        return self.model

    def read_equipment(self):
        print(self.__view.render())