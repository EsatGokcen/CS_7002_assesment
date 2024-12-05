class WorkoutZoneView:

    def __init__(self, workout_zone_model):
        self.__model = workout_zone_model

    def render(self):

        equipments = ",\n".join(str(equipment) for equipment in self.__model.get_list_of_equipments())

        return (
            f"\nWorkout Zone Type: {self.__model.get_workout_zone_type()}"
            f"\nWorkout Zone Capacity: {self.__model.get_workout_zone_capacity()}"
            f"\nAvailable Equipments:\n{equipments} " # SHOULD I ADD LIST OF EQUIPMENTS TO MODEL OR CONTROLLER ?
        )

