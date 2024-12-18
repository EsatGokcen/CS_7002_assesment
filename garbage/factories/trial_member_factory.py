from garbage.factories.abstract_member_factory import MemberFactory
from garbage.members.trial_member_model import TrialMemberModel


class TrialMemberFactory(MemberFactory):

    def create_member(self, name: str, email: str, health_info: str, trial_period: int):
        return TrialMemberModel(name, email, health_info, trial_period)