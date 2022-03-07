from app_api import *

from utils.misc import *
from data.config import *
from GUI import *


def on_startup(connection):
    try:
        connection.set_up()
        MainWindow(title='Vendetta', themename=theme).mainloop()
    except Exception as exc:
        ErrorWindow(title='Error window', themename=theme).mainloop()
    else:
        event_loop.close()
        connection.close()


if __name__ == '__main__':
    on_startup(connection)
