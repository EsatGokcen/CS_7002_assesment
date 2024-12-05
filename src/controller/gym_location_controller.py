from src.model.gym_location_model import GymLocationModel
from src.model.manager_model import GymManagerModel
from src.model.workout_zone_model import WorkoutZoneModel
from src.view.gym_location_view import GymLocationView

class GymLocationController:

    # Handle CRUD (Create, Read, Update, Delete) operations for gym locations and workout zones.

    def __init__(self):
        self.__gym_locations = []
        self.__gym_managers = []
        self.__workout_zones = []
        self.__gym_location_views = []

    def create_gym_manager(self, name: str):
        manager = GymManagerModel(name)
        self.__gym_managers.append(manager)
        return manager

    def create_workout_zone(self, type: str, capacity: int): # NOW IN ITS OWN CONTROLLER
        workout_zone = WorkoutZoneModel(type, capacity)
        self.__workout_zones.append(workout_zone)
        return workout_zone

    def create_gym_location(self, city: str, workout_zones: list[WorkoutZoneModel], manager: GymManagerModel):
        if all(zone in self.__workout_zones for zone in workout_zones) and manager in self.__gym_managers:
            gym_location = GymLocationModel(city, workout_zones, manager)
            gym_location_view = GymLocationView(gym_location)
            self.__gym_locations.append(gym_location)
            self.__gym_location_views.append(gym_location_view)
            return gym_location
        #else:
            #raise ValueError("Workout_zones and/or manager not registered")

    def read_gym_location_views(self):
        for view in self.__gym_location_views:
            print(view.render())





