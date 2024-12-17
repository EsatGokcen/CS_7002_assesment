import unittest

from src.controller.manager_controller import ManagerController


class TestManager(unittest.TestCase):

    def test_create_manager(self):
        manager_controller = ManagerController()
        manager_controller.create_manager(name="Esat")

        # Validate that manager creation was successful
        self.assertTrue(manager_controller.model.get_manager_name(), "Esat")
