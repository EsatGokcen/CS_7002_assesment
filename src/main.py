from src.controller.gym_location_controller import GymLocationController
from src.model.gym_location_model import GymLocationModel
from src.model.gym_manager_model import GymManagerModel
from src.model.gym_workout_zone_model import WorkoutZoneModel
from src.view.gym_location_view import GymLocationView


def main():

    gym_location_controller = GymLocationController()

    # Managers
    manager1 = gym_location_controller.create_gym_manager("Esat")

    # Workout Zones
    workout_zone1 = gym_location_controller.create_workout_zone("Yoga Zone", 15)
    workout_zone2 = gym_location_controller.create_workout_zone("Weight Lifting Zone", 20)
    workout_zone3 = gym_location_controller.create_workout_zone("Power Lifting Zone", 10)

    workout_zones = [workout_zone1, workout_zone2, workout_zone3]

