import setup
import shutil
from data.config import theme
from utils.misc.connection import connection

from frames.authWindow import AuthorizationWindow
from frames.mainWindow import MainWindow
from frames.errorWindow import ErrorWindow


def on_startup(connect):
    try:
        connect.set_up()
    except Exception as exc:
        MainWindow(title='Vendetta', themename=theme, connection=connect).mainloop()
        # ErrorWindow(title='Error window', themename=theme, connection=connection, exception=exc).mainloop()
        connect.close()
    else:
        # AuthorizationWindow(title='Auth form vendetta', themename=theme)
        MainWindow(title='Vendetta', themename=theme, connection=connect).mainloop()
    finally:
        #shutil.rmtree(setup.temp_path + '/img')
        connect.close()


if __name__ == '__main__':
    on_startup(connection)
