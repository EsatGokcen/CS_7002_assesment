import unittest

from src.controller.workout_zone_controller import WorkoutZoneController


class TestWorkoutZone(unittest.TestCase):

    def test_create_workout_zone(self):
        workout_zone_controller = WorkoutZoneController()
        workout_zone = workout_zone_controller.create_workout_zone(type="cardio", capacity=20)

        # Validate that workout zone creation was successful

        self.assertEqual(workout_zone_controller.model, workout_zone, "Workout zone is not created as expected!")

        # these were implemented wrong as they do not check for "cardio" and 20 specifically!
        #self.assertTrue(workout_zone_controller.model.get_workout_zone_type(), "cardio")
        #self.assertTrue(workout_zone_controller.model.get_workout_zone_capacity(), 20)

    def test_create_equipment(self):
        pass