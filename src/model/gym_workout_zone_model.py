
class WorkoutZoneModel:

    def __init__(self, type, capacity):
        self.__type = type
        self.__capacity = capacity

    def get_workout_zone_type(self):
        return self.__type

    def get_workout_zone_capacity(self):
        return self.__capacity