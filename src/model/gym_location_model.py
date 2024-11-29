from src.model.gym_manager_model import GymManagerModel
from src.model.gym_workout_zone_model import WorkoutZoneModel


class GymLocationModel:

    initial_id = 100

    def __init__(self, city: str, workout_zones: list[WorkoutZoneModel] = None, manager: GymManagerModel = None):
        self.__gym_id = GymLocationModel.initial_id
        GymLocationModel.initial_id += 1 # creates a unique id for each gym location instance
        self.__city = city
        self.__workout_zones = workout_zones
        self.__manager = manager

    def get_gym_id(self):
        return self.__gym_id

    def get_gym_city(self):
        return self.__city

    def get_gym_workout_zones(self):
        return self.__workout_zones

    def get_gym_manager(self):
        return self.__manager

    def set_gym_city(self, city: str):
        self.__city = city

    def set_workout_zone(self, new_workout_zone: WorkoutZoneModel, index: int):
            if new_workout_zone not in self.__workout_zones[index]:
                self.__workout_zones.append(new_workout_zone)

    def set_gym_manager(self, manager: str):
        self.__manager = manager


