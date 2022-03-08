import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from GUI.main_window import MainWindow
from GUI.auth_window import AuthorizationWindow
from GUI.error_window import ErrorWindow


from data.config import theme
from utils.misc.connection import connection


def on_startup(connection):
    try:
        connection.set_up()
    except Exception as exc:
        ErrorWindow(title='Error window', themename=theme).mainloop()
        connection.close()
    else:
        # AuthorizationWindow(title='Auth form vendetta', themename=theme)
        MainWindow(title='Vendetta', themename=theme, connection=connection).mainloop()
    finally:
        connection.close()


if __name__ == '__main__':
    on_startup(connection)
