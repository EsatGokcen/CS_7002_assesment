from src.controller.equipment_controller import EquipmentController
from src.controller.gym_controller import GymController
from src.controller.staff_controller import StaffController


def main():
    staff1 = StaffController()
    staff1.create_staff(name="Joey", email="joey@gmail.com", job_title="Personal Trainer")

    staff2 = StaffController()
    staff2.create_staff(name="Rosa", email="rosa@gmail.com", job_title="Nutritionist")

    staff1.read_staff()
    staff2.read_staff()

    gym_controller = GymController()
    gym_controller.create_manager("Esat")

    equipment1 = EquipmentController()
    equipment1.create_equipment(name="Bench Press", type="Strength Training")

    equipment2 = EquipmentController()
    equipment2.create_equipment(name="Squat Rack", type="Strength Training")

    equipment3 = EquipmentController()
    equipment3.create_equipment(name="Dead-lift Platform", type="Strength Training")

    list_of_equipments = [equipment1.model, equipment2.model, equipment3.model]

    gym_controller.create_workout_zone("Strength Training", 20, list_of_equipments)

    gym_controller.read_gym()

if __name__ == '__main__':
    main()


