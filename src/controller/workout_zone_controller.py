from src.model.workout_zone_model import WorkoutZoneModel
from src.view.workout_zone_view import WorkoutZoneView
from src.controller.equipment_controller import EquipmentController


class WorkoutZoneController:

    def __init__(self):
        self.model = WorkoutZoneModel("Yoga Zone", 15)
        self.__view = WorkoutZoneView(self.model)

    def create_workout_zone(self, type: str, capacity: int): # REMOVE FROM gym_location_controller
        self.model.set_type(type)
        self.model.set_capacity(capacity)
        return self.model

    def create_equipment(self, connection: EquipmentController, name: str, type: str):
        equipment = connection.create_equipment(name, type)
        self.model.set_equipment(equipment)

    def read_workout_zone(self):
        print(self.__view.render())






