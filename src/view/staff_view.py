from src.model.staff_model import StaffModel


class StaffView:

    def __init__(self, staff_model: StaffModel):
        self.__model = staff_model

    def render(self):
        return (
            f"\nStaff ID: {self.__model.get_staff_id()}"
            f"\nStaff Name: {self.__model.get_name()}"
            f"\nStaff Email: {self.__model.get_email()}"
            f"\nJob Title: {self.__model.get_job_title()}"
        )