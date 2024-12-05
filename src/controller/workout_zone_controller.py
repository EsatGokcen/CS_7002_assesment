from src.model.workout_zone_model import WorkoutZoneModel
from src.view.workout_zone_view import WorkoutZoneView
from src.controller.equipment_controller import EquipmentController


class WorkoutZoneController:

    def __init__(self):
        self.__model = WorkoutZoneModel("Yoga Zone", 15)
        self.__view = WorkoutZoneView(self.__model)

    def create_workout_zone(self, type: str, capacity: int): # REMOVE FROM gym_location_controller
        self.__model.set_type(type)
        self.__model.set_capacity(capacity)

    def create_equipment(self, connection: EquipmentController, name: str, type: str):
        equipment = connection.create_equipment(name, type)
        self.__model.set_equipment(equipment)

    def read_workout_zone(self):
        print(self.__view.render())

    def read_equipment(self):
        print(self.__view.equipment_render())

    # TO - DO :

    # MAKE SURE THE REST OF THE CODE USES THE NEW CONTROLLER AND VIEWER APPROPRIATELY



