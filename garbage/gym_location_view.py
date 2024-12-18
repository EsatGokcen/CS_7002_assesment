
class GymLocationView:

    def __init__(self, gym_location):
        self.__gym_location = gym_location

    def render(self):
        zones = ", ".join(str(zone) for zone in self.__gym_location.get_gym_workout_zones())
        manager = self.__gym_location.get_gym_manager()
        return (
            f"GYM ID: {self.__gym_location.get_gym_id()}\n"
            f"GYM City: {self.__gym_location.get_gym_city()}\n"
            f"Workout Zones: [{zones}]\n"
            f"GYM Manager: {manager}\n"
        )
