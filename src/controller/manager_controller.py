from src.model.gym_manager_model import GymManagerModel


class ManagerController:

    def __init__(self):
        self.__model = GymManagerModel(name="Placeholder")
        self.__view = None

    def create_manager(self, name: str):
        self.__model.set_manager_name(name)

    def read_manager(self):
        pass