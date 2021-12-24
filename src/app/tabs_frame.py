
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from chats_frame import ChatsFrame

from pathlib import Path


class TabsFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super(TabsFrame, self).__init__(parent, **kwargs)
        self.configure(padding=1)

        self.style = ttk.Style()
        self.style.configure('secondary.TButton', borderwidth=0)

        self.parent = parent

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
                                   command=self._news_button_pressing)
        self.news_btn.pack(side=TOP)

        self.profile_btn = ttk.Button(self, bootstyle=SECONDARY,
                                      image='profile',
                                      padding=0,
                                      takefocus=0,
                                      command=self._profile_button_pressing)
        self.profile_btn.pack(side=TOP, pady=5)

        self.chats_btn = ttk.Button(self, bootstyle=SECONDARY,
                                    image='chats',
                                    padding=0,
                                    takefocus=0,
                                    command=self._chats_button_pressing)
        self.chats_btn.pack(side=TOP)

        self.music_btn = ttk.Button(self, bootstyle=SECONDARY,
                                    image='music',
                                    padding=0,
                                    takefocus=0,
                                    command=self._music_button_pressing)
        self.music_btn.pack(side=TOP, pady=5)

        self.settings_btn = ttk.Button(self, bootstyle=SECONDARY,
                                       image='settings',
                                       padding=0,
                                       takefocus=0,
                                       command=self._settings_button_pressing)
        self.settings_btn.pack(side=BOTTOM)

    def _news_button_pressing(self):
        [i.state(['!pressed']) for i in self.pack_slaves() if 'pressed' in i.state()]
        [i.destroy() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe']

        self.news_btn.state(['pressed'])

    def _profile_button_pressing(self):
        [i.state(['!pressed']) for i in self.pack_slaves() if 'pressed' in i.state()]
        [i.destroy() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe']

        self.profile_btn.state(['pressed'])

    def _chats_button_pressing(self):
        [i.state(['!pressed']) for i in self.pack_slaves() if 'pressed' in i.state()]
        [i.destroy() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe']

        self.chats_btn.state(['pressed'])

        ChatsFrame(self.parent).pack(side=LEFT, expand=FALSE, fill=BOTH, padx=5)

    def _music_button_pressing(self):
        [i.state(['!pressed']) for i in self.pack_slaves() if 'pressed' in i.state()]
        [i.destroy() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe']

        self.music_btn.state(['pressed'])

    def _settings_button_pressing(self):
        [i.state(['!pressed']) for i in self.pack_slaves() if 'pressed' in i.state()]
        [i.destroy() for i in self.parent.pack_slaves() if str(i) != '.!tabsframe']

        self.settings_btn.state(['pressed'])


if __name__ == '__main__':
    root = ttk.Window(title='Tabs Frame', themename='superhero')
    TabsFrame(root).pack()
    root.mainloop()