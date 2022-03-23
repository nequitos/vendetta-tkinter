from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from client.app_api.scrolled_widgets import YScrolledFrame
from client.frames.dialogFrame import DialogFrame

from pathlib import Path


class ChatsFrame(YScrolledFrame):
    def __init__(self, parent, connection, **kwargs):
        super(ChatsFrame, self).__init__(parent, **kwargs)
        self.configure(padding=0)
        self.canvas.configure(width=128)

        self.style = ttk.Style()
        self.style.configure('secondary.TButtons', borderwidth=0)

        self.parent = parent
        self.connection = connection
        self.dialogue_frame = DialogFrame(parent, connection=connection)

        # ----- Images
        image_files = {
            'create': 'create.png',
            'main': 'main.png'
        }
        self.photo_images = []
        img_path = Path(__file__).parent.absolute() / 'icons'
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

        self.dialogue_frame.dialog_name = 'main'
        self.dialogue_frame.pack(side=LEFT, expand=TRUE, fill=BOTH, anchor=CENTER)


if __name__ == '__main__':
    from client.utils.misc.connection import connection

    root = ttk.Window(title='Chats Frame')
    ChatsFrame(root, connection=connection).pack()
    root.mainloop()
