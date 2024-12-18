import unittest

from garbage.member_controller import MemberController


class TestMembers(unittest.TestCase):

    def test_create_regular_member(self):
        # DOES NOT WORK
        member_controller = MemberController()
        #member_controller.create_member(member_type="regular", name="Esra", email="esra@mail.com", health_info="healthy")

        #regular_member_model = RegularMemberModel()
        #self.assertTrue(regular_member_model.get_details(), "Esra", "esra@mail.com", "healthy")