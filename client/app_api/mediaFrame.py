from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from client.handlers.mediaHandler import MediaHandler


class MediaFrame(ttk.Frame):
    def __init__(self, parent, media_file, *args, **kwargs):
        super(MediaFrame, self).__init__(parent, *args, **kwargs)
        self.cancel = None

        self.media_label = ttk.Label(self, bootstyle=INFO, cursor='hand2')
        self.media_label.pack(side=RIGHT, fill=BOTH)

        self.progressbar = ttk.Progressbar(self, orient=HORIZONTAL, mode=DETERMINATE, length=280)

        media_handler = MediaHandler(self.media_label, media_file)
        self.media_label.bind('<Button-1>', media_handler.toggle)

        media_handler.play()