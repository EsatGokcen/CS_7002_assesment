from src.model.gym_location_model import GymLocationModel
from src.model.gym_manager_model import GymManagerModel
from src.model.gym_workout_zone_model import WorkoutZoneModel
from src.view.gym_location_view import GymLocationView

class GymLocationController:

    def __init__(self, gym_locations = None, gym_managers = None, workout_zones = None):
        self.__gym_locations = gym_locations or []
        self.__gym_managers = gym_managers or []
        self.__workout_zones = workout_zones or []
        self.__gym_location_views = [GymLocationView(gym_location) for gym_location in self.__gym_locations]

    def create_gym_manager(self, name: str):
        manager = GymManagerModel(name)
        self.__gym_managers.append(manager)

    def create_workout_zone(self, type: str, capacity: int):
        workout_zone = WorkoutZoneModel(type, capacity)
        self.__workout_zones.append(workout_zone)

    def create_gym_location(self, city: str, workout_zones: list[WorkoutZoneModel], manager: GymManagerModel):
        if all(zone in self.__workout_zones for zone in workout_zones) and manager in self.__gym_managers:
            gym_location = GymLocationModel(city, workout_zones, manager)
            self.__gym_locations.append(gym_location)
            return gym_location
        else:
            raise ValueError("Workout_zones and/or manager not registered")





