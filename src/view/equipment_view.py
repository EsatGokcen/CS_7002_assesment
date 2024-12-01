
class EquipmentView:

    def __init__(self, equipment_model):
        self.__model = equipment_model

    def render(self):
        return(
            f"Equipment Name: {self.__model.get_equipment_name()}"
            f"Equipment Type: {self.__model.get_equipment_type()}"
        )