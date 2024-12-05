from src.model.gym_manager_model import GymManagerModel

class ManagerView:

    def __init__(self, manager_model: GymManagerModel):
        self.__model = manager_model

    def render(self):
        return (
            f"\nManager ID: {self.__model.get_manager_id()}"
            f"\nManager Name: {self.__model.get_manager_name()}"
        )