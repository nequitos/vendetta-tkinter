from ttkbootstrap.constants import *
import ttkbootstrap as ttk


class MediaPlayer(ttk.Frame):
    def __init__(self, parent, media_file, *args, **kwargs):
        super(MediaPlayer, self).__init__(parent, *args, **kwargs)
        self.parent = parent

        #self.media_handler = MediaHandler(media_file=media_file, size=())

        self.media_label = ttk.Label(self)
        self.media_label.pack(side=TOP)

        self.control_frame = ttk.Frame(self)
        self.control_frame.pack(fill=X)

        self.scroll_next = ttk.Button(self.control_frame, bootstyle=OUTLINE,
                                      text='next',
                                      takefocus=0)
        self.scroll_next.pack(side=RIGHT)

        self.btn_play = ttk.Button(self.control_frame, bootstyle=OUTLINE,
                                   text='play',
                                   takefocus=0)
        self.btn_play.pack(side=RIGHT)

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
                                    command=self.on_sound_btn)
        self.sound_btn.pack(side=LEFT)

        self.sound_scale = ttk.Scale(self.control_frame, length=100, orient=HORIZONTAL)

    def on_sound_btn(self):
        try:
            self.sound_scale.pack_info()
        except Exception as exc:
            self.sound_scale.pack(side=LEFT)
        else:
            self.sound_scale.pack_forget()


if __name__ == '__main__':
    root = ttk.Window(title='Media Player', themename='superhero')
    MediaPlayer(root, 'pass').pack()
    root.mainloop()
