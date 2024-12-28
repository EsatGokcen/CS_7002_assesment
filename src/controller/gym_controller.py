from garbage.members.abstract_member_model import MemberModel
from src.controller.manager_controller import ManagerController
from src.controller.staff_controller import StaffController
from src.controller.workout_zone_controller import WorkoutZoneController
from src.model.classes_model import ClassesModel
from src.model.equipment_model import EquipmentModel
from src.model.gym_model import GymModel
from src.model.manager_model import GymManagerModel
from src.model.staff_model import StaffModel
from src.model.workout_zone_model import WorkoutZoneModel
from src.view.gym_view import GymView
from typing import Type


class GymController:

    def __init__(self):
        self.model = GymModel(city="London", manager=None)
        self.__view = GymView(self.model)

    def create_manager(self, name: str) -> GymManagerModel:
        manager_controller = ManagerController()
        manager = manager_controller.create_manager(name)
        self.model.set_gym_manager(manager)
        return manager

    def create_workout_zone(self, type: str, capacity: int, attendant: StaffModel, list_of_equipments: list[EquipmentModel]) -> WorkoutZoneModel:

        # CREATE WORKOUT ZONE
        workout_zone_controller = WorkoutZoneController()
        workout_zone = workout_zone_controller.create_workout_zone(type, capacity)
        workout_zone.set_attendant(attendant)

        self.model.add_workout_zone(workout_zone)

        # ADD LIST OF EQUIPMENTS TO WORKOUT ZONE
        for equipment in list_of_equipments:
            workout_zone.set_equipment(equipment)

        return workout_zone

    def create_staff(self, name: str, email: str, job_title: str) -> StaffModel:
        staff_controller = StaffController()
        staff = staff_controller.create_staff(name, email, job_title)
        self.model.add_staff(staff)
        return staff

    def create_member(self, member: Type[MemberModel]) -> Type[MemberModel]: # adds an already created member to the list
        self.model.add_member(member)
        return member

    def create_class(self, gym_class: ClassesModel) -> ClassesModel: # adds an already created class to the list
        self.model.add_class(gym_class)
        return gym_class

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