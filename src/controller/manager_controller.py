from src.model.manager_model import GymManagerModel
from src.view.manager_view import ManagerView


class ManagerController:

    def __init__(self):
        self.model = GymManagerModel(name="Placeholder")
        self.__view = ManagerView(self.model)

    def create_manager(self, name: str, username: str, password: str) -> GymManagerModel:
        self.model.set_manager_name(name)
        self.model.set_username(username)
        self.model.set_password(password)
        return self.model

    def read_manager(self):
        print(self.__view.render())