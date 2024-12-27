import unittest

from src.controller.member_controller import MemberController


class TestMember(unittest.TestCase):

    def test_create_trial_member(self):

        member_controller = MemberController()
        trial_member1 = member_controller.create_trial_member(name="Tim",
                                                              email="tim@gmail.com",
                                                              phone_number="7393313233",
                                                              username="timsaxaphonist",
                                                              password="Soprano35!")

        self.assertEqual(member_controller.model, trial_member1, "trial member not created as expected")