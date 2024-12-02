from src.model.gym_workout_zone_model import WorkoutZoneModel
from src.view.workout_zone_view import WorkoutZoneView


class WorkoutZoneController:

    def __init__(self):
        self.__model = WorkoutZoneModel("Yoga Zone", 15)
        self.__view = WorkoutZoneView
        self.__list_of_equipments = []

    def create_workout_zone(self, type: str, capacity: int): # REMOVE FROM gym_location_controller
        self.__model.set_type(type)
        self.__model.set_capacity(capacity)


    def read_workout_zone(self):
        pass

    # TO - DO :

    # MIGRATE WORKOUT ZONE MODEL METHODS THAT BETTER SUIT CONTROLLER TO HERE
    # IMPLEMENT WORKOUT ZONE VIEW
    # MAKE SURE THE REST OF THE CODE USES THE NEW CONTROLLER AND VIEWER APPROPRIATELY



