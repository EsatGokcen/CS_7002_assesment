from src.model.equipment_model import EquipmentModel
from src.view.equipment_view import EquipmentView


class EquipmentController:

    def __init__(self):
        self.model = EquipmentModel
        self.__view = EquipmentView(self.model)

    def create_equipment(self, name: str, type: str) -> EquipmentModel:
        equipment = self.model(name=name, type=type)
        return equipment

    def read_equipment(self):
        print(self.__view.render())