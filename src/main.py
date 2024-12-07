from src.controller.equipment_controller import EquipmentController
from src.controller.gym_location_controller import GymLocationController
from src.controller.manager_controller import ManagerController
from src.controller.member_controller import MemberController
from src.controller.workout_zone_controller import WorkoutZoneController


def main():

    member_controller = MemberController()

    member_controller.create_member("premium", "Esat", "esat@mail.com", "Blind", True)
    member_controller.create_member("regular", "Taha", "taha@hotmail.com", "Healthy", "y") # ERROR EXTRA ARGUMENT
    member_controller.create_member("trial", "Tahsin", "tahsin@gmail.com", "Deaf", 7, 8)    # ERROR EXTRA ARGUMENT

    member_controller.read_member() # ERROR PRINTS OBJECT LOCATION INSTEAD OF STRING

    """

    manager1 = ManagerController()
    manager2 = ManagerController()

    manager1.create_manager("Esat")
    manager2.create_manager("Eda")

    manager1.read_manager()
    manager2.read_manager()



    workout_zone_controller = WorkoutZoneController()
    equipment1 = EquipmentController()
    equipment2 = EquipmentController()

    workout_zone_controller.create_workout_zone(type="Trampoline", capacity=32)

    workout_zone_controller.create_equipment(connection=equipment1, name="Trampoline", type="Bouncy things")
    workout_zone_controller.create_equipment(connection=equipment2, name="Bench Press", type="Weight Lifting")

    workout_zone_controller.read_workout_zone()


    equipment_controller = EquipmentController()

    equipment_controller.create_equipment("Bench Press", "Machine")
    equipment_controller.read_equipment()

    

    gym_location_controller = GymLocationController()

    # Create Instances

    # Managers
    manager1 = gym_location_controller.create_gym_manager("Esat")
    manager2 = gym_location_controller.create_gym_manager("Taha")

    # Equipment

    # equipment1 =

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
    
    """

if __name__ == '__main__':
    main()


