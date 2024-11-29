from src.controller.gym_location_controller import GymLocationController

def main():

    gym_location_controller = GymLocationController()

    # Managers
    manager1 = gym_location_controller.create_gym_manager("Esat")
    manager2 = gym_location_controller.create_gym_manager("Taha")
    print("managers created successfully.")

    # Workout Zones
    workout_zone1 = gym_location_controller.create_workout_zone("Yoga Zone", 15)
    workout_zone2 = gym_location_controller.create_workout_zone("Weight Lifting Zone", 20)
    workout_zone3 = gym_location_controller.create_workout_zone("Power Lifting Zone", 10)
    print("workout zones created successfully")

    workout_zones1 = [workout_zone1, workout_zone2, workout_zone3]
    workout_zones2 = [workout_zone3, workout_zone2]
    print("workout zones grouped successfully")

    # Gym Locations
    gym_location_controller.create_gym_location("London", workout_zones1, manager1)
    gym_location_controller.create_gym_location("Istanbul", workout_zones2, manager2)
    print("gym locations created successfully")

    print(gym_location_controller.read_gym_location_views())
    print("gym location view called successfully")

if __name__ == '__main__':
    main()


