from src.client.app_api import *


class ErrorWindow(ttk.Window):
    def __init__(self, connection, exception, **kwargs):
        super(ErrorWindow, self).__init__(**kwargs)
        self.connection = connection
        self.exception = exception


if __name__ == '__main__':
    ErrorWindow(title='Error Window', connection=None).mainloop()
