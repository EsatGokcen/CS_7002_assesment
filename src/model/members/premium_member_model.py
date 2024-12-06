from src.model.members.abstract_member_model import MemberModel


class PremiumMemberModel(MemberModel):

    def __init__(self, name: str, email: str, health_info: str, premium_status: bool = True):
        super().__init__(name, email, health_info)
        self.__premium_status = premium_status
        if self.__premium_status is True:
            self.__membership_status = "Premium member"
        else:
            self.__membership_status = "Regular member"

    def get_details(self):
        return (
            self.__id, self.__name, self.__email, self.__health_info, self.__membership_status
        )

    def set_details(self, name: str, email: str, health_info: str, premium_status: bool):
        self.__name = name
        self.__email = email
        self.__health_info = health_info
        self.__premium_status = premium_status

    def set_premium_status(self, premium_status: bool):
        self.__premium_status = premium_status

