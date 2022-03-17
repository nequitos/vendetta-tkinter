from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from client.frames.tabsFrame import TabsFrame

from pathlib import Path


class MainWindow(ttk.Window):
    def __init__(self, connection, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.minsize(width=202, height=550)
        self.connection = connection

        self.full_screen_state = False
        self.bind('<F11>', self.toggle_full_screen)
        self.bind('<Escape>', self.end_full_screen)

        _icon_path = str(Path(__file__).parent.absolute()) + '/icons/fsociety.gif'
        icon_photo = ttk.PhotoImage(file=_icon_path)
        self.iconphoto(FALSE, icon_photo)

        tabs_frame = TabsFrame(self, connection=connection)
        tabs_frame.pack(side=LEFT, fill=BOTH)

        tabs_frame.chats_button_pressing()
        tabs_frame.chats_frame.main_button_pressing()

        self.update_idletasks()

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.attributes('-fullscreen', self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = False
        self.attributes('-fullscreen', self.full_screen_state)


if __name__ == '__main__':
    from client.utils.misc.connection import connection

    MainWindow(title='Vendetta', connection=connection).mainloop()
