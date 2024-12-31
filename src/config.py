from src.controller.classes_controller import ClassesController
from src.controller.equipment_controller import EquipmentController
from src.controller.gym_controller import GymController
from src.controller.member_controller import MemberController
from src.controller.workout_zone_controller import WorkoutZoneController


def create_workout_zone_data():
    # WORKOUT ZONE 1 - Strength Training

    # EQUIPMENT CREATION
    equipment1 = EquipmentController()
    equipment1.create_equipment(name="Bench Press", type="Strength Training")

    equipment2 = EquipmentController()
    equipment2.create_equipment(name="Squat Rack", type="Strength Training")

    equipment3 = EquipmentController()
    equipment3.create_equipment(name="Dead-lift Platform", type="Strength Training")

    list_of_equipments = [equipment1.model, equipment2.model, equipment3.model]

    strength_zone = WorkoutZoneController()
    strength_zone.create_workout_zone(type="Strength Training",
                                      capacity=10,
                                      list_of_equipments=list_of_equipments)

    # WORKOUT ZONE 2 - Cardio

    # EQUIPMENT CREATION
    equipment4 = EquipmentController()
    equipment4.create_equipment("Treadmill", "Cardio")

    equipment5 = EquipmentController()
    equipment5.create_equipment("Stationary Bicycle", "Cardio")

    equipment6 = EquipmentController()
    equipment6.create_equipment("Rowing Machine", "Cardio")

    list_of_equipments2 = [equipment4.model, equipment5.model, equipment6.model]

    cardio_zone = WorkoutZoneController()
    cardio_zone.create_workout_zone(type="Cardio",
                                    capacity=20,
                                    list_of_equipments= list_of_equipments2)

    # WORKOUT ZONE 3 - Free Weights

    # EQUIPMENT CREATION
    equipment7 = EquipmentController()
    equipment7.create_equipment("Dumbbells", "Free Weights")

    equipment8 = EquipmentController()
    equipment8.create_equipment("Barbells", "Free Weights")

    equipment9 = EquipmentController()
    equipment9.create_equipment("Weight Trees", "Free Weights")

    list_of_equipments3 = [equipment7.model, equipment8.model, equipment9.model]

    free_weights_zone = WorkoutZoneController()
    free_weights_zone.create_workout_zone(type="Free Weights",
                                          capacity=25,
                                          list_of_equipments=list_of_equipments3)

    # WORKOUT ZONE 4 - Stretching

    # EQUIPMENT CREATION
    equipment10 = EquipmentController()
    equipment10.create_equipment("Yoga Mats", "Stretching")

    equipment11 = EquipmentController()
    equipment11.create_equipment("Medicine Balls", "Stretching")

    equipment12 = EquipmentController()
    equipment12.create_equipment("Stretching Straps", "Stretching")

    list_of_equipments4 = [equipment10.model, equipment11.model, equipment12.model]

    stretching_zone = WorkoutZoneController()
    stretching_zone.create_workout_zone(type="Stretching",
                                        capacity=15,
                                        list_of_equipments=list_of_equipments4)

    # WORKOUT ZONE 5 - Combat Zone

    # EQUIPMENT CREATION
    equipment13 = EquipmentController()
    equipment13.create_equipment("Punching Bags", "Combat")

    equipment14 = EquipmentController()
    equipment14.create_equipment("Sparring Rings", "Combat")

    equipment15 = EquipmentController()
    equipment15.create_equipment("Skipping Ropes", "Combat")

    list_of_equipments5 = [equipment13.model, equipment14.model, equipment15.model]

    combat_zone = WorkoutZoneController()
    combat_zone.create_workout_zone(type="Combat Zone",
                                    capacity=10,
                                    list_of_equipments=list_of_equipments5)

    # WORKOUT ZONE 6 - Group Fitness

    # EQUIPMENT CREATION
    equipment16 = EquipmentController()
    equipment16.create_equipment("Spin Bikes", "Group Fitness")

    equipment17 = EquipmentController()
    equipment17.create_equipment("Stability Balls", "Group Fitness")

    equipment18 = EquipmentController()
    equipment18.create_equipment("Sound System and Mirrors", "Group Fitness")

    list_of_equipments6 = [equipment16.model, equipment17.model, equipment18.model]

    group_fitness_zone = WorkoutZoneController()
    group_fitness_zone.create_workout_zone(type="Group Fitness",
                                           capacity=15,
                                           list_of_equipments=list_of_equipments6)

    list_of_workout_zones = [strength_zone.model, cardio_zone.model, free_weights_zone.model,
                             stretching_zone.model, combat_zone.model, group_fitness_zone.model]

    return list_of_workout_zones

def create_member_data():

    member_controller = MemberController()
    trial_member1 = member_controller.create_trial_member(name="Tim",
                                                          email="tim@gmail.com",
                                                          phone_number="7393313233",
                                                          username="timsaxaphonist",
                                                          password="Soprano35!")

    regular_member1 = member_controller.create_regular_member(name="Jack",
                                                              email="jack@gmail.com",
                                                              phone_number="7494414244",
                                                              username="strongjack",
                                                              password="BenchPress120kg!")

    premium_member1 = member_controller.create_premium_member(name="Lucy",
                                                              email="lucy@gmail.com",
                                                              phone_number="7595515255",
                                                              username="Lucy_does_yoga",
                                                              password="India130798")

    trial_member2 = member_controller.create_trial_member(name="Derek",
                                                          email="derek@hotmail.com",
                                                          phone_number="7949957763",
                                                          username="fitDerek",
                                                          password="ILoveMyMum!")

    regular_member2 = member_controller.create_regular_member(name="Alice",
                                                              email="alice@gmail.com",
                                                              phone_number="7292325587",
                                                              username="AliceMalice",
                                                              password="CottonCandy!")

    premium_member2 = member_controller.create_premium_member(name="David",
                                                              email="david@outlook.com",
                                                              phone_number="7595345543",
                                                              username="DavidMalt",
                                                              password="TechCEO!")

    list_of_members = [trial_member1, trial_member2, regular_member1, regular_member2, premium_member1, premium_member2]

    return list_of_members

def create_gym_data():

    members = create_member_data()
    workout_zones = create_workout_zone_data()

    # GYM 1 DATA ;

    # GYM CREATION
    gym1 = GymController()
    gym1.create_manager(name="Esat",username="AdminEsat", password="Admin1000!")

    # STAFF CREATION
    personal_trainer = gym1.create_staff(name="Joey", email="joey@gmail.com", job_title="Personal Trainer")
    gym1.create_staff(name="Rosa", email="rosa@gmail.com", job_title="Nutritionist")

    # MEMBER ADDITION
    gym1.create_member(members[0])
    gym1.create_member(members[2])
    gym1.create_member(members[4])

    # WORKOUT ZONE ADDITION
    gym1.add_workout_zone(workout_zones[0])
    gym1.add_workout_zone(workout_zones[1])
    gym1.add_workout_zone(workout_zones[2])
    gym1.add_workout_zone(workout_zones[4])

    # CREATE A CLASS FOR GYM
    bench_press_class = ClassesController()
    bench_press_class.create_class("Bench Press Class", "28/12/24", 10,
                                   teacher=personal_trainer, location= workout_zones[0])

    bench_press_class.add_attendee(members[2])
    bench_press_class.add_attendee(members[4])

    gym1.create_class(bench_press_class.model)

    # GYM 2 DATA ;

    # GYM CREATION
    gym2 = GymController()
    gym2.model.set_gym_city("Manchester")
    gym2.create_manager(name="Zak", username="ZakAfron", password="KittyCat!")

    # STAFF CREATION
    personal_trainer2 = gym2.create_staff(name="Jocy", email="jocy@fitness.com", job_title="Personal Trainer")
    gym2.create_staff(name="Bob", email="bob@eathealthy.com", job_title="Nutritionist")

    # MEMBER ADDITION
    gym2.create_member(members[1])
    gym2.create_member(members[3])
    gym2.create_member(members[5])

    # WORKOUT ZONE ADDITION
    gym1.add_workout_zone(workout_zones[0])
    gym1.add_workout_zone(workout_zones[1])
    gym1.add_workout_zone(workout_zones[2])
    gym1.add_workout_zone(workout_zones[3])
    gym1.add_workout_zone(workout_zones[5])

    # CLASS CREATION
    cardio_class = ClassesController()
    cardio_class.create_class(name="Cardio Class",
                              date="01/01/2025",
                              capacity=15,
                              teacher=personal_trainer2,
                              location=workout_zones[1])

    cardio_class.add_attendee(members[3])
    cardio_class.add_attendee(members[5])

    gym2.create_class(cardio_class.model)

    return [gym1, gym2]