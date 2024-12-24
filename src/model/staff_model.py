class StaffModel:

    initial_staff_id = 12345

    def __init__(self, job_title: str):
        self.__staff_id = StaffModel.initial_staff_id
        StaffModel.initial_staff_id += 1
        self.__job_title = job_title

    def get_staff_id(self) -> int:
        return self.__staff_id

    def get_job_title(self) -> str:
        return self.__job_title

    def set_job_title(self, job_title: str):
        self.__job_title = job_title