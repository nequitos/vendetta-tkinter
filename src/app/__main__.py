import logging
import time

from utils import *

from pathlib import Path
from client.handler import BasicDispatchClient


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

        self.update_idletasks()

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.attributes('-fullscreen', self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = False
        self.attributes('-fullscreen', self.full_screen_state)


class TabsFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super(TabsFrame, self).__init__(parent, **kwargs)
        self.configure(padding=0)

        self.style = ttk.Style()
        self.style.configure('secondary.TButton', borderwidth=0)

        self.parent = parent
        self.chats_frame = ChatsFrame(self.parent)

        # ----- Images
        image_files = {
            'news': 'news.png',
            'profile': 'profile.png',
            'chats': 'chats.png',
            'music': 'music.png',
            'settings': 'settings.png'
        }
        self.photo_images = []
        img_path = Path(__file__).parent / 'icons'
        for k, v in image_files.items():
            _path = img_path / v
            self.photo_images.append(ttk.PhotoImage(name=k, file=_path))

        # ----- Buttons
        self.news_btn = ttk.Button(self, bootstyle=SECONDARY,
                                   image='news',
                                   padding=0,
                                   takefocus=0,
                                   command=self.news_button_pressing)
        self.news_btn.pack(side=TOP)

        self.profile_btn = ttk.Button(self, bootstyle=SECONDARY,
                                      image='profile',
                                      padding=0,
                                      takefocus=0,
                                      command=self.profile_button_pressing)
        self.profile_btn.pack(side=TOP, pady=5)

        self.chats_btn = ttk.Button(self, bootstyle=SECONDARY,
                                    image='chats',
                                    padding=0,
                                    takefocus=0,
                                    command=self.chats_button_pressing)
        self.chats_btn.pack(side=TOP)

        self.music_btn = ttk.Button(self, bootstyle=SECONDARY,
                                    image='music',
                                    padding=0,
                                    takefocus=0,
                                    command=self.music_button_pressing)
        self.music_btn.pack(side=TOP, pady=5)

        self.settings_btn = ttk.Button(self, bootstyle=SECONDARY,
                                       image='settings',
                                       padding=0,
                                       takefocus=0,
                                       command=self.settings_button_pressing)
        self.settings_btn.pack(side=BOTTOM)

        self.update_idletasks()

    def news_button_pressing(self):
        [i.state(['!pressed']) for i in self.pack_slaves() if 'pressed' in i.state()]
        [i.pack_forget() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe']

        self.news_btn.state(['pressed'])

    def profile_button_pressing(self):
        [i.state(['!pressed']) for i in self.pack_slaves() if 'pressed' in i.state()]
        [i.pack_forget() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe']

        self.profile_btn.state(['pressed'])

    def chats_button_pressing(self):
        [i.state(['!pressed']) for i in self.pack_slaves() if 'pressed' in i.state()]
        [i.pack_forget() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe']

        self.chats_btn.state(['pressed'])

        self.chats_frame.pack(side=LEFT, expand=FALSE, fill=BOTH, padx=5)

    def music_button_pressing(self):
        [i.state(['!pressed']) for i in self.pack_slaves() if 'pressed' in i.state()]
        [i.pack_forget() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe']

        self.music_btn.state(['pressed'])

    def settings_button_pressing(self):
        [i.state(['!pressed']) for i in self.pack_slaves() if 'pressed' in i.state()]
        [i.pack_forget() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe']

        self.settings_btn.state(['pressed'])


class ChatsFrame(ScrolledFrame):
    def __init__(self, parent, **kwargs):
        super(ChatsFrame, self).__init__(parent, **kwargs)
        self.configure(padding=0)
        self.canvas.configure(width=128)

        self.style = ttk.Style()
        self.style.configure('secondary.TButtons', borderwidth=0)

        self.parent = parent
        self.dialogue_frame = DialogFrame(parent)

        # ----- Images
        image_files = {
            'create': 'create.png',
            'main': 'main.png'
        }
        self.photo_images = []
        img_path = Path(__file__).parent / 'icons'
        for k, v in image_files.items():
            _path = img_path / v
            self.photo_images.append(ttk.PhotoImage(name=k, file=_path))

        # ----- Buttons
        self.create_btn = ttk.Button(self.interior, bootstyle=SECONDARY,
                                     image='create',
                                     padding=0,
                                     takefocus=0,
                                     command=self.create_button_pressing)
        self.create_btn.pack(side=TOP)

        self.main_btn = ttk.Button(self.interior, bootstyle=SECONDARY,
                                   image='main',
                                   padding=0,
                                   takefocus=0,
                                   command=self.main_button_pressing)
        self.main_btn.pack(side=TOP)

        self.update_idletasks()

    def create_button_pressing(self):
        [i.state(['!pressed']) for i in self.interior.pack_slaves() if 'pressed' in i.state()]
        [i.pack_forget() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe' and str(i) != '.!chatsframe']

        self.create_btn.state(['pressed'])

    def main_button_pressing(self):
        [i.state(['!pressed']) for i in self.interior.pack_slaves() if 'pressed' in i.state()]
        [i.pack_forget() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe' and str(i) != '.!chatsframe']

        self.main_btn.state(['pressed'])

        self.dialogue_frame.pack(side=LEFT, expand=TRUE, fill=BOTH, anchor=CENTER)


class DialogFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super(DialogFrame, self).__init__(parent, **kwargs)
        self.configure(padding=0)

        style = ttk.Style()

        self.parent = parent

        # ----- Notebook
        self.notebook = notebook = ttk.Notebook(self)

        self.info_button = info_button = ttk.Button(notebook, bootstyle=SECONDARY,
                                                    text='View pinned.',
                                                    takefocus=0,
                                                    padding=5)
        self.voice_button = voice_button = ttk.Button(notebook, bootstyle=SECONDARY,
                                                      text='Record a voice message.',
                                                      takefocus=0,
                                                      padding=5)
        self.media_button = media_button = ttk.Button(notebook, bootstyle=SECONDARY,
                                                      takefocus=0,
                                                      text='Select media.',
                                                      padding=5)

        self.notebook.add(info_button, text='Info')
        self.notebook.add(voice_button, text='Voice')
        self.notebook.add(media_button, text='Media')

        self.notebook.pack(side=TOP, fill=X)

        # ----- Messages Frame
        self.messages_frame = ScrolledFrame(self)
        self.messages_frame.pack(side=TOP, expand=TRUE, fill=BOTH)

        # ----- Text Frame
        self.scrolled_text = ScrolledText(self)
        self.scrolled_text.text.config(height=3)
        self.scrolled_text.text.bind('<Return>', self.send_message)
        self.scrolled_text.pack(side=LEFT, expand=TRUE, fill=BOTH)

        # ----- Control Frame
        control_frame = ttk.Frame(self)
        control_frame.pack(side=RIGHT, expand=FALSE, fill=BOTH)

        self.update_idletasks()

    def send_message(self, event):
        message = self.scrolled_text.text.get(1.0, END).strip()

        message_frame_line = ttk.Frame(self.messages_frame.interior, bootstyle=INFO)
        message_frame_line.pack(side=TOP, expand=TRUE, fill=X)

        message_frame_line_label = ttk.Label(message_frame_line, text=message)
        message_frame_line_label.pack(side=RIGHT, fill=BOTH)

        loop.run_until_complete(connection.send_data(data=message))
        self.scrolled_text.text.delete(1.0, END)

    def recv_message(self):
        pass


class LoginFrame(ttk.Window):
    def __init__(self, **kwargs):
        super(LoginFrame, self).__init__(**kwargs)
        self.resizable(FALSE, FALSE)
        self.geometry('400x200')

        login_label = ttk.Label(text='Login:')
        login_label.grid(row=0, column=0, columnspan=1, sticky=W, padx=10, pady=10)

        password_label = ttk.Label(text='Password:')
        password_label.grid(row=1, column=0, columnspan=1, sticky=W, padx=10, pady=10)

        login_entry = ttk.Entry(width=50)
        login_entry.grid(row=0, column=1, columnspan=3, sticky=W)

        password_entry = ttk.Entry(width=50)
        password_entry.grid(row=1, column=1, columnspan=3, sticky=W)

        auto_login_check_btn = ttk.Checkbutton(text='auto login')
        auto_login_check_btn.grid(row=2, column=1, sticky=E, pady=5)

        forgot_password_label = ttk.Label(bootstyle=INFO,
                                          text='Forgot password?',
                                          justify=CENTER,
                                          cursor='hand2')
        forgot_password_label.bind('<Button-1>', self.password_recovery)
        forgot_password_label.grid(row=3, column=1, columnspan=2, sticky=W)

        registration_btn = ttk.Button(bootstyle=SECONDARY,
                                      text='registration')
        registration_btn.grid(row=4, column=0, columnspan=1, sticky=E)

        login_btn = ttk.Button(bootstyle=SECONDARY,
                               text='login')
        login_btn.grid(row=4, column=2, columnspan=3)

        self.update_idletasks()

    def password_recovery(self, event):
        pass


class ErrorWindow(ttk.Window):
    def __init__(self, **kwargs):
        super(ErrorWindow, self).__init__(**kwargs)


if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG,
        filename='logs/' + time.ctime().replace(':', '.') + '.log'
    )
    logger_ttk = logging.Logger('ttk')
    logger_connection = logging.Logger('connection')

    try:
        connection = BasicDispatchClient()
        loop = connection.event_loop
        connection.start_client()

        Application(title='Vendetta', themename='superhero').mainloop()
    except Exception as ex:
        print(ex)
    finally:
        pass




