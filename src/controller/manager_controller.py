from src.model.manager_model import GymManagerModel
from src.view.manager_view import ManagerView


class ManagerController:

    def __init__(self):
        self.model = GymManagerModel(name="Placeholder")
        self.__view = ManagerView(self.model)

    def create_manager(self, name: str) -> GymManagerModel:
        self.model.set_manager_name(name)
        return self.model

    def read_manager(self):
        print(self.__view.render())