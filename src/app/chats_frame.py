

from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from pathlib import Path


class ChatsFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super(ChatsFrame, self).__init__(parent, **kwargs)
        self.configure(padding=1)

        self.style = ttk.Style()
        self.style.configure('secondary.TButtons', borderwidth=0)

        self.parent = parent

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
        self.create_btn = ttk.Button(self, bootstyle=SECONDARY,
                                     image='create',
                                     padding=0,
                                     takefocus=0,)
        self.create_btn.pack(side=TOP)

        self.main_btn = ttk.Button(self, bootstyle=SECONDARY,
                                   image='main',
                                   padding=0,
                                   takefocus=0)
        self.main_btn.pack(side=TOP, pady=5)

    def _create_button_pressing(self):
        pass

    def _main_button_settings(self):
        pass


if __name__ == '__main__':
    root = ttk.Window(title='Chats Frame', themename='superhero')
    ChatsFrame(root).pack()
    root.mainloop()