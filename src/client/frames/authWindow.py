from src.client.app_api import *
from src.client.frames.loginFrame import *


class AuthorizationWindow(ttk.Window):
    def __init__(self, connection, **kwargs):
        super(AuthorizationWindow, self).__init__(**kwargs)
        self.resizable(FALSE, FALSE)
        self.connection = connection

        self.full_screen_state = False
        self.bind('<F11>', self.toggle_full_screen)
        self.bind('<Escape>', self.end_full_screen)

        LoginFrame(self, connection).pack()

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.attributes('-fullscreen', self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = False
        self.attributes('-fullscreen', self.full_screen_state)


if __name__ == '__main__':
    AuthorizationWindow(title='Auth from vendetta', connection='sss', themename='superhero').mainloop()