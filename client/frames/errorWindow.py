import ttkbootstrap as ttk


class ErrorWindow(ttk.Window):
    def __init__(self, connection, exception, **kwargs):
        super(ErrorWindow, self).__init__(**kwargs)
        self.connection = connection
        self.exception = exception


if __name__ == '__main__':
    from client.utils.misc.connection import connection

    ErrorWindow(title='Error Window', connection=connection, exception=None).mainloop()
