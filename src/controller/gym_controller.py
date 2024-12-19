from src.controller.manager_controller import ManagerController
from src.controller.workout_zone_controller import WorkoutZoneController
from src.model.equipment_model import EquipmentModel
from src.model.gym_model import GymModel
from src.model.manager_model import GymManagerModel
from src.model.workout_zone_model import WorkoutZoneModel
from src.view.gym_view import GymView


class GymController:

    def __init__(self):
        self.model = GymModel(city="London", manager=None)
        self.__view = GymView(self.model)

    def create_manager(self, name: str) -> GymManagerModel:
        manager_controller = ManagerController()
        manager = manager_controller.create_manager(name)
        self.model.set_gym_manager(manager)
        return manager

    # NEED TO BE ABLE TO ADD EQUIPMENT TO WORKOUT ZONES
    def create_workout_zone(self, type: str, capacity: int, list_of_equipments: list[EquipmentModel]) -> WorkoutZoneModel:

        # CREATE WORKOUT ZONE
        workout_zone_controller = WorkoutZoneController()
        workout_zone = workout_zone_controller.create_workout_zone(type, capacity)
        self.model.add_workout_zone(workout_zone)

        # ADD LIST OF EQUIPMENTS TO WORKOUT ZONE
        for equipment in list_of_equipments:
            workout_zone.set_equipment(equipment)

        return workout_zone

    def update_city(self, city: str) -> str:
        self.model.set_gym_city(city)
        return self.model.get_gym_city()

    def update_manager(self, name: str) -> GymManagerModel:
        manager_controller = ManagerController()
        manager = manager_controller.create_manager(name)
        self.model.set_gym_manager(manager)
        return manager

    def read_gym(self):
        print(self.__view.render())