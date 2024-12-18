from src.model.manager_model import GymManagerModel
from src.model.workout_zone_model import WorkoutZoneModel


class GymModel:

    initial_id = 100

    def __init__(self, city: str, manager: GymManagerModel = None):
        self.__id = GymModel.initial_id
        GymModel.initial_id += 1
        self.__city = city
        self.__manager = manager
        self.__workout_zones = []
        self.__list_of_staff = []
        self.__list_of_members = []
        self.__list_of_classes = []

    def get_gym_id(self):
        return self.__id

    def get_gym_city(self):
        return self.__city

    def get_gym_manager(self):
        return self.__manager

    def get_gym_workout_zones(self):
        for workout_zone in self.__workout_zones:
            return workout_zone

    def get_list_of_staff(self):
        for staff in self.__list_of_staff:
            return staff

    def get_list_of_members(self):
        for member in self.__list_of_members:
            return member

    def get_list_of_classes(self):
        for gym_class in self.__list_of_classes:
            return gym_class

    def set_gym_city(self, city: str):
        self.__city = city

    def set_gym_manager(self, manager: GymManagerModel):
        self.__manager = manager

    def add_workout_zone(self, workout_zone: WorkoutZoneModel):
        self.__workout_zones.append(workout_zone)

    def add_staff(self, staff):
        self.__list_of_staff.append(staff) # NEED TO CREATE A CLASS FOR STAFF

    def add_member(self, member):
        self.__list_of_members.append(member) # NEED TO CREATE A NEW WORKING MEMBER CLASS

    def add_class(self, gym_class):
        self.__list_of_classes.append(gym_class) # NEED TO CREATE A CLASS FOR GYM CLASSES