from src.client.app_api import *


class ErrorWindow(ttk.Window):
    def __init__(self, connection, **kwargs):
        super(ErrorWindow, self).__init__(**kwargs)
        self.connection = connection


if __name__ == '__main__':
    ErrorWindow(title='Error Window', connection=None).mainloop()
