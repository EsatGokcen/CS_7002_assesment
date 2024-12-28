from src.model.classes_model import ClassesModel


class ClassesView:

    def __init__(self, classes_model: ClassesModel):
        self.__model = classes_model

    def render(self):

        list_of_attendees = self.__model.get_attendees()
        attendees = ", ".join(str(attendee) for attendee in list_of_attendees)

        return (
            f"\nClass Name: {self.__model.get_name()}"
            f"\nClass Date: {self.__model.get_date()}"
            f"\nClass Location: {self.__model.get_location()}"
            f"\nClass Teacher: {self.__model.get_teacher()}"
            f"\nClass Capacity: {self.__model.get_capacity()}"
            f"\nClass Attendees: {attendees}"
        )