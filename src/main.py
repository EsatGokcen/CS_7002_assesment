from src.config import create_gym_data
from src.view.tkinter.tk_controller import TkController


def main():

    # TKINTER
    app = TkController(create_gym_data())
    app.start()

if __name__ == '__main__':
    main()


