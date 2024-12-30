from src.controller.classes_controller import ClassesController
from src.controller.equipment_controller import EquipmentController
from src.controller.gym_controller import GymController
from src.controller.member_controller import MemberController


def create_data():

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
    gym_controller = GymController()
    gym_controller.create_manager(name="Esat",username="AdminEsat", password="Admin1000!")

    personal_trainer = gym_controller.create_staff(name="Joey", email="joey@gmail.com", job_title="Personal Trainer")
    gym_controller.create_staff(name="Rosa", email="rosa@gmail.com", job_title="Nutritionist")

    gym_controller.create_member(trial_member1)
    gym_controller.create_member(regular_member1)
    gym_controller.create_member(premium_member1)

    strength_zone = gym_controller.create_workout_zone(type="Strength Training",
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
    gym_controller.create_class(bench_press_class.model)

    return gym_controller.read_gym()