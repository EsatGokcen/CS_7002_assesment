from src.controller.gym_location_controller import GymLocationController
from src.model.gym_location_model import GymLocationModel
from src.model.gym_manager_model import GymManagerModel
from src.model.gym_workout_zone_model import WorkoutZoneModel
from src.view.gym_location_view import GymLocationView


def main():

    gym_location_controller = GymLocationController()
    manager1 = gym_location_controller.create_gym_manager(GymManagerModel("Esat"))
    workout_zone1 = gym_location_controller.create_workout_zone(WorkoutZoneModel())



    gym_location_model = GymLocationModel("London")
    gym_location_view = GymLocationView(gym_location_model)
