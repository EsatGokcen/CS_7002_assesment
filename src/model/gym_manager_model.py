
class GymManagerModel:

    initial_manager_id = 1000

    def __init__(self, name: str):
        self.__manager_id = GymManagerModel.initial_manager_id
        GymManagerModel.initial_manager_id += 1 # creates a unique id for each manager
        self.__name = name

    def __str__(self):
        return f"Gym Manager: {self.__name}"

    def get_manager_id(self):
        return self.__manager_id

    def get_manager_name(self):
        return self.__name

    def set_manager_name(self, name: str):
        self.__name = name
