from src.model.member_model import MemberModel


class RegularMemberModel(MemberModel):

    def __init__(self, name: str, email: str, phone_number: str):
        super().__init__(name=name, email=email, phone_number=phone_number)
        self.__member_type = "regular"

    def get_member_type(self) -> str:
        return self.__member_type