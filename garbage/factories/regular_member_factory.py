from garbage.factories.abstract_member_factory import MemberFactory
from garbage.members.regular_member_model import RegularMemberModel


class RegularMemberFactory(MemberFactory):

    def create_member(self, name: str, email: str, health_info: str):
        return RegularMemberModel(name, email, health_info)
