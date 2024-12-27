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

    def test_create_regular_member(self):

        member_controller = MemberController()
        regular_member1 = member_controller.create_regular_member(name="Jack",
                                                              email="jack@gmail.com",
                                                              phone_number="7494414244",
                                                              username="strongjack",
                                                              password="BenchPress120kg!")

        self.assertEqual(member_controller.model, regular_member1, "regular member not created as expected")

    def test_create_premium_member(self):

        member_controller = MemberController()
        premium_member1 = member_controller.create_premium_member(name="Lucy",
                                                              email="lucy@gmail.com",
                                                              phone_number="7595515255",
                                                              username="Lucy_does_yoga",
                                                              password="India130798")

        self.assertEqual(member_controller.model, premium_member1, "premium member not created as expected")