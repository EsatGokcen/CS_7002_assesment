import unittest

from src.controller.equipment_controller import EquipmentController

class TestEquipment(unittest.TestCase):

    def test_create_equipment(self):
        equipment1 = EquipmentController()
        equipment1.create_equipment(name="Bench Press", type="Barbell Weights")

        # Validate that equipment creation was successful

        self.assertEqual(equipment1.model.get_equipment_name(), "Bench Press", "Equipment is not created as expected!")
        self.assertEqual(equipment1.model.get_equipment_type(), "Barbell Weights", "Equipment is not created as expected!")

        # These are unnecessary here as they only check if method returns True
        #self.assertTrue(equipment_controller.model.get_equipment_name(), "Bench Press")
        #self.assertTrue(equipment_controller.model.get_equipment_type(), "Barbell Weights")
