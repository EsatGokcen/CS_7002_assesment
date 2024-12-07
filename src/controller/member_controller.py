from src.factories.premium_member_factory import PremiumMemberFactory
from src.factories.regular_member_factory import RegularMemberFactory
from src.factories.trial_member_factory import TrialMemberFactory
from src.view.member_view import MemberView


class MemberController:

    def __init__(self):
        self.__factories = {
            "premium": PremiumMemberFactory,
            "regular": RegularMemberFactory,
            "trial": TrialMemberFactory
        }
        self.__members = []
        self.__view = MemberView

    def create_member(self, member_type: str, *args):
        if member_type == "premium":
            member_factory = self.__factories.get(member_type)
            member_object = member_factory.create_member(*args)
            self.__members.append(member_object)
            return member_object

        elif member_type == "regular":
            member_factory = self.__factories.get(member_type)
            member_object = member_factory.create_member(*args)
            self.__members.append(member_object)
            return member_object

        elif member_type == "trial":
            member_factory = self.__factories.get(member_type)
            member_object = member_factory.create_member(*args)
            self.__members.append(member_object)
            return member_object
        else:
            raise ValueError("Incorrect member type!")

    def read_member(self):
        for member in self.__members:
            view_object = self.__view(member)
            print(view_object.render())