from src.model.member_model import MemberModel


class PremiumMemberModel(MemberModel):

    def __init__(self, name: str, email: str, phone_number: str):
        super().__init__(name=name, email=email, phone_number=phone_number)
        self.__member_type = "premium"
        self.__fee = 50.00 # £ per month

    def __str__(self):
        return f"\nMember ID: x, Name: {self.get_name()}, Member Type: {self.get_member_type()}"

    def get_member_type(self) -> str:
        return self.__member_type

    def get_member_fee(self) -> float:
        return self.__fee

    def set_member_fee(self, fee_amount: float):
        self.__fee = fee_amount