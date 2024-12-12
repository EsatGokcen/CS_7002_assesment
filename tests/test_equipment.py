import unittest

from src.controller.equipment_controller import EquipmentController

class TestEquipment(unittest.TestCase):

    def test_create_equipment(self):
        equipment_controller = EquipmentController()
        equipment_controller.create_equipment(name="Bench Press", type="Barbell Weights")

        # Validate that equipment creation was successful
        self.assertTrue(equipment_controller.model.get_equipment_name(), "Bench Press")
        self.assertTrue(equipment_controller.model.get_equipment_type(), "Barbell Weights")
