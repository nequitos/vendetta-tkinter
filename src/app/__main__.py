

from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from tabs_frame import TabsFrame


class Application(ttk.Window):
    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)
        self.geometry('900x600')
        self.minsize(width=202, height=550)

        self.full_screen_state = False
        self.bind('<F11>', self.toggle_full_screen)
        self.bind('<Escape>', self.end_full_screen)

        icon_photo = ttk.PhotoImage(file='icons/fsociety.gif')
        self.iconphoto(FALSE, icon_photo)

        tabs_frame = TabsFrame(self)
        tabs_frame.pack(side=LEFT, fill=BOTH)

        tabs_frame.chats_button_pressing()
        tabs_frame.chats_frame.main_button_pressing()

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.attributes('-fullscreen', self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = False
        self.attributes('-fullscreen', self.full_screen_state)


if __name__ == '__main__':
    Application(title='Vendetta Alpha', themename='superhero').mainloop()