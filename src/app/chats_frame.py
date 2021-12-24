

from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from pathlib import Path


class ChatsFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super(ChatsFrame, self).__init__(parent, **kwargs)

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

        self.scrollbar = scrollbar = ttk.Scrollbar(self,
                                       orient=VERTICAL)

        self.canvas = canvas = ttk.Canvas(self,
                                          width=128,
                                          highlightthickness=0,
                                          yscrollcommand=scrollbar.set)
        self.scrollbar.config(command=canvas.yview)
        self.canvas.pack(side=LEFT, fill=BOTH, anchor=CENTER)

        self.interior = interior = ttk.Frame(canvas)
        self.interior_id = canvas.create_window((0, 0), window=interior, anchor=NW)
        self.interior.bind('<Configure>', self._set_scrollbar)

        # ----- Buttons
        self.create_btn = ttk.Button(interior, bootstyle=SECONDARY,
                                     image='create',
                                     padding=0,
                                     takefocus=0,
                                     command=self._create_button_pressing)
        self.create_btn.pack(side=TOP)

        self.main_btn = ttk.Button(interior, bootstyle=SECONDARY,
                                   image='main',
                                   padding=0,
                                   takefocus=0,
                                   command=self._main_button_pressing)
        self.main_btn.pack(side=TOP)

        self.update_idletasks()
        self._main_button_pressing()

    def _set_scrollbar(self, event):
        if self.interior.winfo_height() > self.winfo_height():
            self.canvas.config(scrollregion=self.canvas.bbox(ALL))
            self.scrollbar.pack(side=RIGHT, fill=Y)
        else:
            self.canvas.config(scrollregion=(0, 0, 0, 0))
            self.scrollbar.pack_forget()

    def _create_button_pressing(self):
        [i.state(['!pressed']) for i in self.interior.pack_slaves() if 'pressed' in i.state()]
        [i.destroy() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe' and str(i) != '.!chatsframe']

        self.create_btn.state(['pressed'])

    def _main_button_pressing(self):
        [i.state(['!pressed']) for i in self.interior.pack_slaves() if 'pressed' in i.state()]
        [i.destroy() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe' and str(i) != '.!chatsframe']

        self.main_btn.state(['pressed'])


if __name__ == '__main__':
    root = ttk.Window(title='Chats Frame', themename='superhero')
    ChatsFrame(root).pack(expand=TRUE, fill=BOTH)
    root.mainloop()