
class EquipmentView:

    def __init__(self, equipment_model):
        self.__model = equipment_model

    def render(self):
        return(
            f"\nEquipment Name: {self.__model.get_equipment_name()}"
            f"\nEquipment Type: {self.__model.get_equipment_type()}"
        )