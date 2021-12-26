
from dialog_frame import DialogFrame

from utils import *
from pathlib import Path


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

    def create_button_pressing(self):
        [i.state(['!pressed']) for i in self.interior.pack_slaves() if 'pressed' in i.state()]
        [i.pack_forget() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe' and str(i) != '.!chatsframe']

        self.create_btn.state(['pressed'])

    def main_button_pressing(self):
        [i.state(['!pressed']) for i in self.interior.pack_slaves() if 'pressed' in i.state()]
        [i.pack_forget() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe' and str(i) != '.!chatsframe']

        self.main_btn.state(['pressed'])

        self.dialogue_frame.pack(side=LEFT, expand=TRUE, fill=BOTH, anchor=CENTER)


if __name__ == '__main__':
    root = ttk.Window(title='Chats Frame', themename='superhero')
    ChatsFrame(root).pack(expand=TRUE, fill=BOTH)
    root.mainloop()