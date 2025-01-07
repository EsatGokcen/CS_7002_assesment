from src.controller.classes_controller import ClassesController
from src.controller.equipment_controller import EquipmentController
from src.controller.gym_controller import GymController
from src.controller.member_controller import MemberController
from src.controller.workout_zone_controller import WorkoutZoneController
import copy

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

    trial_member3 = member_controller.create_trial_member(name="Selim",
                                                          email="selim@hotmail.com",
                                                          phone_number="5423768567",
                                                          username="GucluSelim",
                                                          password="AnnemiSeverim!")

    regular_member3 = member_controller.create_regular_member(name="Defne",
                                                              email="defne@gmail.com",
                                                              phone_number="5882543421",
                                                              username="DefneAyranci",
                                                              password="YogaQueen!")

    premium_member3 = member_controller.create_premium_member(name="Mustafa",
                                                              email="mustafa@outlook.com",
                                                              phone_number="5649234581",
                                                              username="MustafaAbi",
                                                              password="BaskanMusti!")

    list_of_members1 = [trial_member1, regular_member1, premium_member1]
    list_of_members2 = [trial_member2, regular_member2, premium_member2]
    list_of_members3 = [trial_member3, regular_member3, premium_member3]

    return (list_of_members1, list_of_members2, list_of_members3)

def create_gym_data():

    members1, members2, members3 = create_member_data()
    workout_zones = create_workout_zone_data()

    # GYM 1 DATA ; ===========================================================================

    # GYM CREATION
    gym1 = GymController()
    gym1.create_manager(name="Esat",username="AdminEsat", password="Admin1000!")

    # STAFF CREATION
    personal_trainer1_gym1 = gym1.create_staff(name="Joey", email="joey@gmail.com", job_title="Personal Trainer")
    personal_trainer2_gym1 = gym1.create_staff(name="Tyson", email="tyson@fury.com", job_title="Personal Trainer")
    personal_trainer3_gym1 = gym1.create_staff(name="Alice", email="alice@gmail.com", job_title="Personal Trainer")
    gym1.create_staff(name="Rosa", email="rosa@gmail.com", job_title="Nutritionist")
    gym1.create_staff(name="Cameron", email="cameron@health.com", job_title="Nutritionist")

    # MEMBER ADDITION
    for member1 in members1:
        gym1.create_member(member1)

    # WORKOUT ZONE ADDITION
    gym1.add_workout_zone(copy.deepcopy(workout_zones[0]))
    gym1.add_workout_zone(copy.deepcopy(workout_zones[1]))
    gym1.add_workout_zone(copy.deepcopy(workout_zones[2]))
    gym1.add_workout_zone(copy.deepcopy(workout_zones[4]))

    # CREATE CLASSES FOR GYM
    bench_press_class_gym1 = ClassesController()
    bench_press_wz_gym1 = workout_zones[0]
    bench_press_wz_gym1.set_attendant(personal_trainer1_gym1)
    bench_press_class_gym1.create_class("Bench Press Class", "13/01/25", 10,
                                   teacher=personal_trainer1_gym1, location= workout_zones[0])
    gym1.create_class(bench_press_class_gym1.model)

    kickboxing_class_gym1 = ClassesController()
    kickboxing_wz_gym1 = workout_zones[4]
    kickboxing_wz_gym1.set_attendant(personal_trainer2_gym1)
    kickboxing_class_gym1.create_class("Kickboxing Class", "15/01/25", 10,
                                  teacher=personal_trainer2_gym1, location=workout_zones[4])
    gym1.create_class(kickboxing_class_gym1.model)

    cardio_class_gym1 = ClassesController()
    cardio_class_wz_gym1 = workout_zones[1]
    cardio_class_wz_gym1.set_attendant(personal_trainer3_gym1)
    cardio_class_gym1.create_class("Cardio Class", "17/01/25", 10,
                                   teacher=personal_trainer3_gym1, location=workout_zones[1])

    # GYM 2 DATA ; ===========================================================================

    # GYM CREATION
    gym2 = GymController()
    gym2.model.set_gym_city("Manchester")
    gym2.create_manager(name="Zak", username="ZakAfron", password="Admin1001!")

    # STAFF CREATION
    personal_trainer1_gym2 = gym2.create_staff(name="Alfie", email="alife@gmail.com", job_title="Personal Trainer")
    personal_trainer2_gym2 = gym2.create_staff(name="Jocy", email="jocy@fitness.com", job_title="Personal Trainer")
    gym2.create_staff(name="Bob", email="bob@eathealthy.com", job_title="Nutritionist")
    gym2.create_staff(name="Lee", email="lee@nutrition.com", job_title="Nutritionist")

    # MEMBER ADDITION
    for member2 in members2:
        gym2.create_member(member2)

    # WORKOUT ZONE ADDITION
    gym2.add_workout_zone(copy.deepcopy(workout_zones[0]))
    gym2.add_workout_zone(copy.deepcopy(workout_zones[1]))
    gym2.add_workout_zone(copy.deepcopy(workout_zones[2]))
    gym2.add_workout_zone(copy.deepcopy(workout_zones[3]))
    gym2.add_workout_zone(copy.deepcopy(workout_zones[5]))

    # CLASS CREATION
    cardio_class_gym2 = ClassesController()
    cardio_class_wz_gym2 = workout_zones[1]
    cardio_class_wz_gym2.set_attendant(personal_trainer2_gym2)
    cardio_class_gym2.create_class(name="Cardio Class",
                              date="11/01/25",
                              capacity=15,
                              teacher=personal_trainer2_gym2,
                              location=workout_zones[1])
    gym2.create_class(cardio_class_gym2.model)

    disco_bike_class_gym2 = ClassesController()
    disco_bike_wz_gym2 = workout_zones[5]
    disco_bike_wz_gym2.set_attendant(personal_trainer1_gym2)
    disco_bike_class_gym2.create_class(name="Disco Bike Class", date="12/01/25", capacity=15,
                                       teacher=personal_trainer1_gym2, location=workout_zones[5])
    gym2.create_class(disco_bike_class_gym2.model)

    yoga_class_gym2 = ClassesController()
    yoga_wz_gym2 = workout_zones[3]
    yoga_wz_gym2.set_attendant(personal_trainer2_gym2)
    yoga_class_gym2.create_class(name="Yoga Class", date="15/01/25", capacity=10,
                                 teacher=personal_trainer2_gym2, location=workout_zones[3])
    gym2.create_class(yoga_class_gym2.model)

    # GYM 3 DATA ; ===========================================================================

    # GYM CREATION
    gym3 = GymController()
    gym3.model.set_gym_city("Istanbul")
    gym3.create_manager(name="Kerem", username="Kerem", password="Admin1002!")

    # STAFF CREATION
    personal_trainer1_gym3 = gym3.create_staff(name="Ozan", email="ozan@gmail.com", job_title="Personal Trainer")
    personal_trainer2_gym3 = gym3.create_staff(name="Zeynep", email="zeynep@gym.com", job_title="Personal Trainer")
    personal_trainer3_gym3 = gym3.create_staff(name="Ali", email="ali@fitness.com", job_title="Personal Trainer")
    gym3.create_staff(name="Asli", email="asli@eathealthy.com", job_title="Nutritionist")
    gym3.create_staff(name="Eda", email="eda@gmail.com", job_title="Nutritionist")

    # MEMBER ADDITION
    for member3 in members3:
        gym3.create_member(member3)

    # WORKOUT ZONE ADDITION
    gym3.add_workout_zone(copy.deepcopy(workout_zones[0]))
    gym3.add_workout_zone(copy.deepcopy(workout_zones[1]))
    gym3.add_workout_zone(copy.deepcopy(workout_zones[2]))
    gym3.add_workout_zone(copy.deepcopy(workout_zones[3]))
    gym3.add_workout_zone(copy.deepcopy(workout_zones[5]))

    # CLASS CREATION
    cardio_class_gym3 = ClassesController()
    cardio_class_gym3.create_class(name="Cardio Class",
                              date="12/01/2025",
                              capacity=15,
                              teacher=personal_trainer3_gym3,
                              location=workout_zones[1])

    gym3.create_class(cardio_class_gym3.model)

    yoga_class_gym3 = ClassesController()
    yoga_class_gym3.create_class(name="Yoga Class", date="15/01/25", capacity=8,
                                 teacher=personal_trainer2_gym3, location=workout_zones[3])
    gym3.create_class(yoga_class_gym3.model)

    bench_press_class_gym3 = ClassesController()
    bench_press_class_gym3.create_class("Bench Press Class", "18/01/25", 10,
                                   teacher=personal_trainer1_gym3, location= workout_zones[0])
    gym3.create_class(bench_press_class_gym3.model)

    return [gym1, gym2, gym3]