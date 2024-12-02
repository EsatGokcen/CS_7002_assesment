from src.model.gym_workout_zone_model import WorkoutZoneModel
from src.view.workout_zone_view import WorkoutZoneView


class WorkoutZoneController:

    def __init__(self):
        self.__model = WorkoutZoneModel
        self.__view = WorkoutZoneView

