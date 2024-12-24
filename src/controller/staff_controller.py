from src.model.staff_model import StaffModel
from src.view.staff_view import StaffView


class StaffController:

    def __init__(self):
        self.model = StaffModel(name="placeholder", email="placeholder", job_title="placeholder")
        self.__view = StaffView(self.model)

    def create_staff(self, name: str, email: str, job_title: str) -> StaffModel:
        self.model.set_name(name)
        self.model.set_email(email)
        self.model.set_job_title(job_title)
        return self.model

    def read_staff(self):
        print(self.__view.render())