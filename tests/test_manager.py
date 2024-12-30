import unittest

from src.controller.manager_controller import ManagerController


class TestManager(unittest.TestCase):

    def test_create_manager(self):
        manager_controller = ManagerController()
        manager = manager_controller.create_manager(name="Esat", username="AdminEsat", password="Admin1000!")

        # Validate that manager creation was successful

        self.assertEqual(manager_controller.model, manager, "Manager is not created as expected!")

        #self.assertTrue(manager_controller.model.get_manager_name(), "Esat")
