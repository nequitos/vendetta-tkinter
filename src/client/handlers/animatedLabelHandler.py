from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from itertools import count, cycle
from PIL import ImageTk


class AnimatedLabelHandler(ttk.Label):
    def __init__(self, parent, widget, filename):
        super(AnimatedLabelHandler, self).__init__(parent)
        self.parent = parent
        self.widget = widget
        self.filename = filename

        self.load(filename)

    def load(self, image):
        cadres = []
        try:
            for i in count(1):
                cadres.append(ImageTk.PhotoImage(image.copy()))
                image.seek(i)
        except EOFError:
            pass

        frames = cycle(cadres)

        try:
            self.delay = image.info['duration']
        except Exception as exc:
            self.delay = 100

        if len(cadres) == 1:
            self.config(image=next(frames))
        else:
            self.next_frame(frames)

    def unload(self, frames):
        self.config(image=None)
        frames = None

    def next_frame(self, frames):
        if frames:
            self.widget.config(image=next(frames))
            self.widget.after(self.delay, lambda: self.next_frame(frames))