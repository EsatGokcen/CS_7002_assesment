from src.controller.equipment_controller import EquipmentController
from src.controller.gym_controller import GymController


def main():

    gym_controller = GymController()
    gym_controller.create_manager("Esat")
    workout_zone = gym_controller.create_workout_zone("Strength Training", 20)


    equipment_controller = EquipmentController()
    equipment = equipment_controller.create_equipment("Bench Press", "Strength Training")
    workout_zone.set_equipment(equipment)

    gym_controller.read_gym()

if __name__ == '__main__':
    main()


