from abc import ABC, abstractmethod

class MemberModel(ABC):

    initial_member_id = 111111 # 6 digit

    def __init__(self, name: str, email: str, phone_number: str):
        self.__id = MemberModel.initial_member_id
        MemberModel.initial_member_id += 1
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__username = "placeholder"
        self.__password = "placeholder"
        self.__health_info = "Healthy"

    @abstractmethod
    def get_member_type(self) -> str:
        pass

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        return self.__email

    def get_phone_number(self) -> str:
        return self.__phone_number

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def get_health_info(self) -> str:
        return self.__health_info

    def set_name(self, name: str):
        self.__name = name

    def set_email(self, email: str):
        self.__email = email

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def set_username(self, username: str):
        self.__username = username

    def set_password(self, password: str):
        self.__password = password

    def set_health_info(self, health_info: str):
        self.__health_info = health_info

