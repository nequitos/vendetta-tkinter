from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from client.handlers.tkMediaHandler import TkMediaHandler

__all__ = [
    'MediaPlayer'
]


class MediaPlayer(ttk.Frame):
    def __init__(self, parent, media_file,  *args, **kwargs):
        super(MediaPlayer, self).__init__(parent, *args, **kwargs)
        self.media_file = media_file
        self.parent = parent

        self.media_label = ttk.Label(self)
        self.media_label.pack(side=TOP)

        self.control_frame = ttk.Frame(self)
        self.control_frame.pack(fill=X)

        self.progressbar = ttk.Progressbar(
            self, orient=HORIZONTAL, length=100, mode=DETERMINATE)
        self.progressbar.pack(side=TOP, fill=X)

        self.btn_play = ttk.Button(self.control_frame, bootstyle=OUTLINE,
                                   text='play',
                                   takefocus=0)
        self.btn_play.pack(side=RIGHT)

        self.scroll_next = ttk.Button(self.control_frame, bootstyle=OUTLINE,
                                      text='next',
                                      takefocus=0)
        self.scroll_next.pack(side=RIGHT)

        self.scroll_back = ttk.Button(self.control_frame, bootstyle=OUTLINE,
                                      text='back',
                                      takefocus=0)
        self.scroll_back.pack(side=RIGHT)

        self.mute_btn = ttk.Button(self.control_frame, bootstyle=OUTLINE,
                                     text='mute',
                                     takefocus=0)
        self.mute_btn.pack(side=LEFT)

        self.sound_btn = ttk.Button(self.control_frame, bootstyle=OUTLINE,
                                    text='sound',
                                    takefocus=0,
                                    command=self.on_sound)
        self.sound_btn.pack(side=LEFT)

        self.sound_scale = ttk.Scale(self.control_frame, length=100, orient=HORIZONTAL)

        self.media_handler = TkMediaHandler(media_file, self.media_label, self.btn_play, self.progressbar)
        self.media_handler.size = self.media_handler.get_size(media_file)
        self.media_handler.handle()

    def on_sound(self):
        try:
            self.sound_scale.pack_info()
        except Exception as exc:
            self.sound_scale.pack(side=LEFT)
        else:
            self.sound_scale.pack_forget()


if __name__ == '__main__':
    root = ttk.Window(title='Media Player', themename='superhero')
    MediaPlayer(root, r'C:\Users\fears\Pictures\200px-Lua-Logo.svg.png').pack()
    root.mainloop()
