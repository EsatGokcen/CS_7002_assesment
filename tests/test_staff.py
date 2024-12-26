import unittest

from src.controller.staff_controller import StaffController


class TestStaff(unittest.TestCase):

    def test_create_staff(self):
        staff1 = StaffController()
        test_variable1 = staff1.create_staff(name="Joey", email="joey@gmail.com", job_title="Personal Trainer")

        staff2 = StaffController()
        test_variable2 = staff2.create_staff(name="Rosa", email="rosa@gmail.com", job_title="Nutritionist")

        self.assertEqual(staff1.model, test_variable1, "staff 1 not created as expected")
        self.assertEqual(staff2.model, test_variable2, "staff 2 not created as expected")



