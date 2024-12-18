import unittest

from src.controller.gym_controller import GymController


class TestGym(unittest.TestCase):

    def test_create_manager(self):
        gym_controller = GymController()
        gym_controller.create_manager("Esat")

        self.assertTrue(gym_controller.model.get_gym_manager(), "Esat") # NOT WORKING -> RETURNS NONE INSTEAD ?

    def test_create_workout_zone(self):
        gym_controller = GymController()
        gym_controller.create_workout_zone("Strength Training", 15)

        self.assertTrue(gym_controller.model.get_gym_workout_zones(), ) # NOT SURE WHAT ARGS TO PUT THROUGH HERE AS msg: