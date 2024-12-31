from src.model.gym_model import GymModel


class GymView:

    def __init__(self, gym_model: GymModel):
        self.__model = gym_model

    def render(self):
        id = self.__model.get_gym_id()
        city = self.__model.get_gym_city()
        manager = self.__model.get_gym_manager()
        workout_zones = self.__model.get_gym_workout_zones()
        equipments_list = self.__model.get_equipments_for_workout_zones()
        staff_list = self.__model.get_list_of_staff()
        members_list = self.__model.get_list_of_members()
        classes_list = self.__model.get_list_of_classes()

        # Gets each workout zone in the list as a string
        zones = ", ".join(str(zone) for zone in workout_zones)
        equipments = "\n".join(str(equipment) for equipment in equipments_list)
        staffs = ", ".join(str(staff) for staff in staff_list)
        members = ", ".join(str(member) for member in members_list)
        classes = ", ".join(str(clas) for clas in classes_list)

        return (
            f"\nGYM ID: {id}"
            f"\nGYM City: {city}"
            f"\nGYM Manager: {manager}"
            f"\nGYM workout zones: {zones}" 
            f"\nEquipments: {equipments}"
            f"\nGYM staff: {staffs}"
            f"\nGYM members: {members}"
            f"\nGYM classes: {classes}"
        )