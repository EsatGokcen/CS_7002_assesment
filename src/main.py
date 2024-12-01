from src.controller.gym_location_controller import GymLocationController

def main():

    gym_location_controller = GymLocationController()

    # Create Instances

    # Managers
    manager1 = gym_location_controller.create_gym_manager("Esat")
    manager2 = gym_location_controller.create_gym_manager("Taha")

    # Workout Zones
    workout_zone1 = gym_location_controller.create_workout_zone("Yoga Zone", 15)
    workout_zone2 = gym_location_controller.create_workout_zone("Weight Lifting Zone", 20)
    workout_zone3 = gym_location_controller.create_workout_zone("Power Lifting Zone", 10)

    workout_zones1 = [workout_zone1, workout_zone2, workout_zone3]
    workout_zones2 = [workout_zone3, workout_zone2]

    # Gym Locations
    gym_location_controller.create_gym_location("London", workout_zones1, manager1)
    gym_location_controller.create_gym_location("Istanbul", workout_zones2, manager2)

    # Call instances

    gym_location_controller.read_gym_location_views()

if __name__ == '__main__':
    main()


