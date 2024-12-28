import unittest

from src.controller.classes_controller import ClassesController
from src.controller.staff_controller import StaffController
from src.controller.workout_zone_controller import WorkoutZoneController


class TestClasses(unittest.TestCase):

    def test_create_class(self):
        # EXAMPLE STAFF
        staff1 = StaffController()
        staff1.create_staff("Tom","tom@gmail.com","personal trainer")

        # EXAMPLE WORKOUT ZONE
        workoutzone = WorkoutZoneController()
        workoutzone.create_workout_zone("Cardio", 20)
        workoutzone.update_attendant(staff1.model)

        # CREATE CLASS
        cardio_class = ClassesController()
        test_variable1 = cardio_class.create_class("Cardio Class", "28/12/24", 20, teacher=staff1.model, location=workoutzone.model)

        self.assertEqual(cardio_class.model, test_variable1, "Class not created as expected!")

