from src.config import create_data
from src.view.tkinter.tk_controller import TkController


def main():

    # TKINTER
    app = TkController(create_data())
    app.start()

    # IDEA pick gym when registering and not in log in
    # when logging in it should already know the gym you've picked at register!

if __name__ == '__main__':
    main()


