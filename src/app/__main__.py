from threading import Thread
from setup import *


class Application(ttk.Window):
    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)
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

        self.update_idletasks()

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.attributes('-fullscreen', self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = False
        self.attributes('-fullscreen', self.full_screen_state)


class AuthorizationWindow(ttk.Window):
    def __init__(self, **kwargs):
        super(AuthorizationWindow, self).__init__(**kwargs)
        self.resizable(FALSE, FALSE)

        self.full_screen_state = False
        self.bind('<F11>', self.toggle_full_screen)
        self.bind('<Escape>', self.end_full_screen)

        LoginFrame(self).pack()

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.attributes('-fullscreen', self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = False
        self.attributes('-fullscreen', self.full_screen_state)


if __name__ == '__main__':
    from tabs_frame import TabsFrame
    from login_frame import LoginFrame

    #AuthorizationWindow(title='Auth window', themename=theme).mainloop()
    #Application(title='Vendetta Alpha', themename=theme).mainloop()

    try:
        connection.set_up()
        logger.debug('Run application')
        try:
            Application(title='Vendetta Alpha', themename=theme).mainloop()
            #LoginWindow(title='Login', themename=theme).mainloop()
        except Exception as exc:
            logger.error('{}'.format(exc))

    except Exception as exc:
        logger.error('{}'.format(exc))
    else:
        logger.debug('Close connection')
        event_loop.close()
        connection.close()
