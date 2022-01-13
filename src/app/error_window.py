from utils import *


class ErrorWindow(ttk.Window):
    def __init__(self, **kwargs):
        super(ErrorWindow, self).__init__(**kwargs)


if __name__ == '__main__':
    from setup import theme

    ErrorWindow(title='Error Window', themename=theme).mainloop()
