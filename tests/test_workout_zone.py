import unittest

from src.controller.workout_zone_controller import WorkoutZoneController


class TestWorkoutZone(unittest.TestCase):

    def test_create_workout_zone(self):
        workout_zone_controller = WorkoutZoneController()
        workout_zone_controller.create_workout_zone(type="cardio", capacity=20)

        # Validate that workout zone creation was successful
        self.assertTrue(workout_zone_controller.model.get_workout_zone_type(), "cardio")
        self.assertTrue(workout_zone_controller.model.get_workout_zone_capacity(), 20)