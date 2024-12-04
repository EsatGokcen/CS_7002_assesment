from src.model.gym_workout_zone_model import WorkoutZoneModel
from src.view.workout_zone_view import WorkoutZoneView
from src.controller.equipment_controller import EquipmentController


class WorkoutZoneController:

    def __init__(self):
        self.__model = WorkoutZoneModel("Yoga Zone", 15)
        self.__view = WorkoutZoneView

    def create_workout_zone(self, type: str, capacity: int): # REMOVE FROM gym_location_controller
        self.__model.set_type(type)
        self.__model.set_capacity(capacity)

    def add_equipment(self, create_equipment: EquipmentController, name: str, type: str):
        equipment = create_equipment.create_equipment(name, type)
        return self.__list_of_equipments.append(equipment)


    def read_workout_zone(self):
        view_object = self.__view(self.__model)
        print(view_object.render())

    # TO - DO :

    # MIGRATE WORKOUT ZONE MODEL METHODS THAT BETTER SUIT CONTROLLER TO HERE
    # IMPLEMENT WORKOUT ZONE VIEW
    # MAKE SURE THE REST OF THE CODE USES THE NEW CONTROLLER AND VIEWER APPROPRIATELY



