from src.controller.classes_controller import ClassesController
from src.controller.equipment_controller import EquipmentController
from src.controller.gym_controller import GymController
from src.controller.member_controller import MemberController


def create_data():

    # GYM 1 DATA ;

    # EQUIPMENT CREATION
    equipment1 = EquipmentController()
    equipment1.create_equipment(name="Bench Press", type="Strength Training")

    equipment2 = EquipmentController()
    equipment2.create_equipment(name="Squat Rack", type="Strength Training")

    equipment3 = EquipmentController()
    equipment3.create_equipment(name="Dead-lift Platform", type="Strength Training")

    list_of_equipments = [equipment1.model, equipment2.model, equipment3.model]

    # MEMBER CREATION
    member_controller = MemberController()
    trial_member1 = member_controller.create_trial_member(name="Tim",
                                                          email="tim@gmail.com",
                                                          phone_number="7393313233",
                                                          username="timsaxaphonist",
                                                          password="Soprano35!")

    #member_controller.read_member(trial_member1)

    regular_member1 = member_controller.create_regular_member(name="Jack",
                                                              email="jack@gmail.com",
                                                              phone_number="7494414244",
                                                              username="strongjack",
                                                              password="BenchPress120kg!")

    #member_controller.read_member(regular_member1)

    premium_member1 = member_controller.create_premium_member(name="Lucy",
                                                              email="lucy@gmail.com",
                                                              phone_number="7595515255",
                                                              username="Lucy_does_yoga",
                                                              password="India130798")

    #member_controller.read_member(premium_member1)

    # GYM CREATION
    gym1 = GymController()
    gym1.create_manager(name="Esat",username="AdminEsat", password="Admin1000!")

    personal_trainer = gym1.create_staff(name="Joey", email="joey@gmail.com", job_title="Personal Trainer")
    gym1.create_staff(name="Rosa", email="rosa@gmail.com", job_title="Nutritionist")

    gym1.create_member(trial_member1)
    gym1.create_member(regular_member1)
    gym1.create_member(premium_member1)

    strength_zone = gym1.create_workout_zone(type="Strength Training",
                                                       capacity=20,
                                                       attendant=personal_trainer,
                                                       list_of_equipments=list_of_equipments)

    # CREATE A CLASS FOR GYM
    bench_press_class = ClassesController()
    bench_press_class.create_class("Bench Press Class", "28/12/24", 10,
                                   teacher=personal_trainer, location= strength_zone)

    bench_press_class.add_attendee(premium_member1)
    bench_press_class.add_attendee(regular_member1)

    #bench_press_class.read_class()
    gym1.create_class(bench_press_class.model)

    # GYM 2 DATA ;

    # EQUIPMENT CREATION
    equipment4 = EquipmentController()
    equipment4.create_equipment("Treadmill", "Cardio")

    equipment5 = EquipmentController()
    equipment5.create_equipment("Stationary Bicycle", "Cardio")

    equipment6 = EquipmentController()
    equipment6.create_equipment("Rowing Machine", "Cardio")

    list_of_equipments2 = [equipment4.model, equipment5.model, equipment6.model]

    # MEMBER CREATION
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

    # GYM CREATION
    gym2 = GymController()
    gym2.model.set_gym_city("Manchester")
    gym2.create_manager(name="Zak", username="ZakAfron", password="KittyCat!")

    personal_trainer2 = gym2.create_staff(name="Jocy", email="jocy@fitness.com", job_title="Personal Trainer")
    gym2.create_staff(name="Bob", email="bob@eathealthy.com", job_title="Nutritionist")

    gym2.create_member(trial_member2)
    gym2.create_member(regular_member2)
    gym2.create_member(premium_member2)

    cardio_zone = gym2.create_workout_zone(type="Cardio",
                                           capacity=20,
                                           attendant=personal_trainer2,
                                           list_of_equipments= list_of_equipments2)

    # CLASS CREATION
    cardio_class = ClassesController()
    cardio_class.create_class(name="Cardio Class",
                              date="01/01/2025",
                              capacity=15,
                              teacher=personal_trainer2,
                              location=cardio_zone)

    cardio_class.add_attendee(regular_member2)
    cardio_class.add_attendee(premium_member2)

    gym2.create_class(cardio_class.model)

    return [gym1, gym2]