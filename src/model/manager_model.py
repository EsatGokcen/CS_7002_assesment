
class GymManagerModel:

    initial_manager_id = 1000

    def __init__(self, name: str):
        self.__manager_id = GymManagerModel.initial_manager_id
        GymManagerModel.initial_manager_id += 1 # creates a unique id for each manager
        self.__name = name
        self.__username = "admin"
        self.__password = "admin"

    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__manager_id}"

    def get_manager_id(self) -> int:
        return self.__manager_id

    def get_manager_name(self) -> str:
        return self.__name

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def set_manager_name(self, name: str):
        self.__name = name

    def set_username(self, username: str):
        self.__username = username

    def set_password(self, password: str):
        self.__password = password

