import unittest

from src.controller.gym_controller import GymController


class TestGym(unittest.TestCase):

    def test_create_manager(self):
        gym_controller = GymController()
        gym_controller.create_manager("Esat")

        self.assertEqual(gym_controller.model.get_gym_manager() == '', "Manager not created successfully!")
        # USE ASSERT EQUAL INSTEAD OF TRUE AS YOU CAN CHECK RETURN VALUES MORE ACCURATELY

    def test_create_workout_zone(self):
        gym_controller = GymController()
        gym_controller.create_workout_zone("Strength Training", 15)

        self.assertEqual(len(gym_controller.model.get_gym_workout_zones()), 1, "Gym workout zone is not created!" )
        workout_zone = gym_controller.model.get_gym_workout_zones()[0]

