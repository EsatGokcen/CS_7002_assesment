from src.model.member_model import MemberModel
from src.model.premium_member_model import PremiumMemberModel
from src.model.regular_member_model import RegularMemberModel
from src.model.trial_member_model import TrialMemberModel
from src.view.member_view import MemberView


class MemberController:

    def __init__(self):
        self.model = None
        self.__view = MemberView(self.model)

    def create_trial_member(self, name: str, email: str, phone_number: str, username: str, password: str) -> TrialMemberModel:
        self.model = TrialMemberModel(name=name, email=email, phone_number=phone_number)
        self.model.set_username(username)
        self.model.set_password(password)
        return self.model

    def create_regular_member(self, name: str, email: str, phone_number: str, username: str, password: str) -> RegularMemberModel:
        self.model = RegularMemberModel(name=name, email=email, phone_number=phone_number)
        self.model.set_username(username)
        self.model.set_password(password)
        return self.model

    def create_premium_member(self, name: str, email: str, phone_number: str, username: str, password: str) -> PremiumMemberModel:
        self.model = PremiumMemberModel(name=name, email=email, phone_number=phone_number)
        self.model.set_username(username)
        self.model.set_password(password)
        return self.model

    def read_member(self):
        print(self.__view.render())