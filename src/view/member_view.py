from src.model.members.abstract_member_model import MemberModel


class MemberView:

    def __init__(self, member_type: MemberModel):
        self.__member_type = member_type

    def render(self):
        details = self.__member_type.get_details()
        details_str = "\n".join(str(value) for value in details)
        print("\nMEMBER DETAILS: ")
        print(details_str) # KWARGS WOULD WORK SO MUCH BETTER FOR THIS ...
