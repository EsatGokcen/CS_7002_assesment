from src.model.gym_model import GymModel


class GymView:

    def __init__(self, gym_model: GymModel):
        self.__model = gym_model

    def render(self):
        id = self.__model.get_gym_id()
        city = self.__model.get_gym_city()
        manager = self.__model.get_gym_manager()
        workout_zones = self.__model.get_gym_workout_zones()
        staff = self.__model.get_list_of_staff()
        members = self.__model.get_list_of_members()
        classes = self.__model.get_list_of_classes()

        return (
            f"\nGYM ID: {id}"
            f"\nGYM City: {city}"
            f"\nGYM Manager: {manager}"
            f"\nGYM workout zones: {workout_zones}" # returns location instead of items , should list equipments as well
            f"\nGYM staff: {staff}"
            f"\nGYM members: {members}"
            f"\nGYM classes: {classes}"
        )