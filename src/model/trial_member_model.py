from src.model.member_model import MemberModel


class TrialMemberModel(MemberModel):

    def __init__(self, name: str, email: str, phone_number: str):
        super().__init__(name=name, email=email, phone_number=phone_number)
        self.__member_type = "trial"
        self.__trial_period = 7 # DAYS

    def __str__(self):
        return f"\nMember ID: {self.get_id()}, Name: {self.get_name()}, Member Type: {self.get_member_type()}"

    def get_member_type(self) -> str:
        return self.__member_type

    def get_trial_period(self) -> int:
        return self.__trial_period

    def set_trial_period(self, time_amount: int):
        self.__trial_period = time_amount
