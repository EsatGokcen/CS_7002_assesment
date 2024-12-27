from src.model.member_model import MemberModel


class MemberView:

    def __init__(self, member_model: MemberModel):
        self.__model = member_model

    def render(self) -> str:
        return (
            f"\nMember ID: {self.__model.get_id()}"
            f"\nMember Name: {self.__model.get_name()}"
            f"\nMembership Type: {self.__model.get_member_type()}"
            f"\nMember Contact Details:\nNumber: {self.__model.get_phone_number()}\nEmail: {self.__model.get_email()}"
            f"\nMember Login Details:\nUsername: {self.__model.get_username()}\nPassword: {self.__model.get_password()}"
        )