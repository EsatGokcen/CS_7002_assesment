from src.factories.abstract_member_factory import MemberFactory
from src.model.members.premium_member_model import PremiumMemberModel


class PremiumMemberFactory(MemberFactory):

    def create_member(self, name: str, email: str, health_info: str, premium_status: bool = True):
        return PremiumMemberModel(name, email, health_info, premium_status)