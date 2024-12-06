from abc import ABC, abstractmethod

class MemberModel(ABC):

    initial_id = 1111

    def __init__(self, name: str, email: str, health_info: str):
        self.__id = MemberModel.initial_id
        MemberModel.initial_id += 1
        self.__name = name
        self.__email = email
        self.__health_info = health_info

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def set_details(self, *args): # FIX PLS
        pass