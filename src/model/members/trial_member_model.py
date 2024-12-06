from src.model.members.abstract_member_model import MemberModel


class TrialMemberModel(MemberModel):

    def __init__(self, name: str, email: str, health_info: str, trial_period: int):
        super().__init__(name, email, health_info)
        self.__membership_status = "Trial Member"
        self.__trial_period = trial_period

    def get_details(self):
        return (
            self.__id, self.__name, self.__email, self.__health_info, self.__membership_status, self.__trial_period
        )

    def set_details(self, name: str, email: str, health_info: str, trial_period: int):
        self.__name = name
        self.__email = email
        self.__health_info = health_info
        self.__trial_period = trial_period

    def set_trial_period(self, trial_period: int):
        self.__trial_period = trial_period
