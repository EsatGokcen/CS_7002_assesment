import unittest

from src.controller.equipment_controller import EquipmentController
from src.controller.gym_controller import GymController
from src.model.equipment_model import EquipmentModel


class TestGym(unittest.TestCase):

    def test_create_manager(self):
        gym_controller = GymController()
        manager = gym_controller.create_manager("Esat")

        self.assertEqual(gym_controller.model.get_gym_manager() ,manager ,"Manager not created successfully!")
        # USE ASSERT EQUAL INSTEAD OF TRUE AS YOU CAN CHECK RETURN VALUES MORE ACCURATELY

    def test_create_workout_zone(self):
        # equipment_controller = EquipmentController
        # equipment1 = equipment_controller.create_equipment(name="Bench Press", type="Strength Training")
        # ERROR: Parameter 'self' unfilled
        equipment1 = EquipmentModel(name="Bench Press", type="Strength Training")
        equipment2 = EquipmentModel(name="Squat Rack", type="Strength Training")
        equipment3 = EquipmentModel(name="Dead-lift Platform", type="Strength Training")
        list_of_equipments = [equipment1, equipment2, equipment3]

        gym_controller = GymController()
        workout_zones = gym_controller.create_workout_zone("Strength Training", 15, list_of_equipments)

        # CHECKS IF GYM CONTROLLER HAS A WORKOUT ZONE IN ITS LIST
        self.assertEqual(len(gym_controller.model.get_gym_workout_zones()), 1, "Gym workout zone is not created!" )

        # CHECKS IF WORKOUT ZONE IS THE CORRECT ONE IN GYM CONTROLLERS WORKOUT ZONES LIST
        workout_zone = gym_controller.model.get_gym_workout_zones()[0]
        self.assertEqual(workout_zones, workout_zone, "gym workout zone does not have suspected values")

        # CHECKS IF LIST OF EQUIPMENTS IS IN WORKOUT ZONE OBJECT
        self.assertEqual(len(workout_zone.get_list_of_equipments()), 3, "List of equipments not created as expected")
