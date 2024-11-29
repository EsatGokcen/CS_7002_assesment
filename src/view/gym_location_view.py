
class GymLocationView:

    def __init__(self, gym_location_model):
        self.__gym_location_model = gym_location_model

    def refresh(self):
        print(f"Gym ID: {self.__gym_location_model.get_gym_id()}")
        print(f"Gym City: {self.__gym_location_model.get_gym_city()}")
        print(f"Gym Workout Zones: {self.__gym_location_model.get_gym_workout_zones()}")
        print(f"Gym Manager: {self.__gym_location_model.get_gym_manager()}")
