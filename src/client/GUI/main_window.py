from src.client.app_api import *
from .tabs_frame import *


class MainWindow(ttk.Window):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.minsize(width=202, height=550)

        self.full_screen_state = False
        self.bind('<F11>', self.toggle_full_screen)
        self.bind('<Escape>', self.end_full_screen)

        icon_photo = ttk.PhotoImage(file='GUI/icons/fsociety.gif')
        self.iconphoto(FALSE, icon_photo)

        tabs_frame = TabsFrame(self)
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