from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from client.handlers.tkMediaHandler import TkMediaHandler
from client.app_api.mediaPlayer import MediaPlayer

__all__ = [
    'BufferLabel'
]


class BufferLabel(ttk.Label):
    def __init__(self, parent, media_file, *args, **kwargs):
        super(BufferLabel, self).__init__(parent, *args, **kwargs)
        self.toplevel = None
        self.parent = parent
        self.media_file = media_file

        self.media_handler = TkMediaHandler(media_file, self, None)
        self.media_handler.size = self.get_size()
        self.media_handler.insert_start_frame()
        self.bind('<Button-1>', self.on_label)
        self.bind('<Button-3>', lambda _: self.destroy())

    def on_label(self, event=None):
        self.toplevel = ttk.Toplevel()
        self.toplevel.protocol('WM_DELETE_WINDOW', self.off_label)
        media_player = MediaPlayer(self.toplevel, self.media_file)
        media_player.pack()

        self.bind('<Button-1>', self.off_label)

    def off_label(self, event=None):
        self.toplevel.destroy()
        self.bind('<Button-1>', self.on_label)

    def get_size(self):
        width, height = self.media_handler.get_size(self.media_file)

        resized_width = int(float((width / 100) * (10000 / width)))
        resized_height = int(float((height / 100) * (5000 / height)))
        return resized_width, resized_height


if __name__ == '__main__':
    root = ttk.Window(title='Buffer Frame', themename='superhero')
    BufferLabel(root, r'C:\Users\fears\Videos\video.mp4').pack()
    root.mainloop()
