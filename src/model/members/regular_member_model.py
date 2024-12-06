from src.model.members.abstract_member_model import MemberModel


class RegularMemberModel(MemberModel):

    def __init__(self, name: str, email: str, health_info: str):
        super().__init__(name, email, health_info)
        self.__membership_status = "Regular Member"

    def get_details(self):
        return (
            self.__id, self.__name, self.__email, self.__health_info, self.__membership_status
        )

    def set_details(self, name: str, email: str, health_info: str):
        self.__name = name
        self.__email = email
        self.__health_info = health_info
