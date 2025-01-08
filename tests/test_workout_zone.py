import unittest

from src.controller.equipment_controller import EquipmentController
from src.controller.workout_zone_controller import WorkoutZoneController


class TestWorkoutZone(unittest.TestCase):

    def test_create_workout_zone(self):
        workout_zone_controller = WorkoutZoneController()
        workout_zone = workout_zone_controller.create_workout_zone(type="cardio", capacity=20, list_of_equipments=[])

        # Validate that workout zone creation was successful

        self.assertEqual(workout_zone_controller.model, workout_zone, "Workout zone is not created as expected!")

        # these were implemented wrong as they do not check for "cardio" and 20 specifically!
        #self.assertTrue(workout_zone_controller.model.get_workout_zone_type(), "cardio")
        #self.assertTrue(workout_zone_controller.model.get_workout_zone_capacity(), 20)

    def test_create_equipment(self):
        workout_zone_controller = WorkoutZoneController()
        workout_zone = workout_zone_controller.create_workout_zone(type="cardio", capacity=20, list_of_equipments=[])

        equipment_controller = EquipmentController()
        equipment = workout_zone_controller.create_equipment(connection=equipment_controller ,name="Treadmill", type="cardio")

        self.assertEqual(workout_zone_controller.model.get_list_of_equipments()[0], equipment,
                         "Equipment not created and added to workout zone as expected!")




