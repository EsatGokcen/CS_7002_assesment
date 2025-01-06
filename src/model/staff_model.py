from src.model.member_model import MemberModel


class StaffModel:

    initial_staff_id = 12345

    def __init__(self, name: str, email: str,  job_title: str):
        self.__staff_id = StaffModel.initial_staff_id
        StaffModel.initial_staff_id += 1
        self.__name = name
        self.__email = email
        self.__job_title = job_title
        self.__booked_sessions = []

    def __repr__(self):
        return f"\nStaff ID: {self.__staff_id}, Name: {self.__name}, Email: {self.__email}, Job Title: {self.__job_title}"

    def __str__(self):
        return f" Name:{self.__name}, Email: {self.__email}" # Role: {self.__job_title}"

    def get_staff_id(self) -> int:
        return self.__staff_id

    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        return self.__email

    def get_job_title(self) -> str:
        return self.__job_title

    def get_booked_sessions(self) -> list[MemberModel]:
        return self.__booked_sessions

    def set_name(self, name: str):
        self.__name = name

    def set_email(self, email: str):
        self.__email = email

    def set_job_title(self, job_title: str):
        self.__job_title = job_title

    def add_member_to_session(self, member: MemberModel):
        self.__booked_sessions.append(member)