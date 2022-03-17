from ttkbootstrap.constants import *
import ttkbootstrap as ttk


class BufferFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(BufferFrame, self).__init__(parent, *args, **kwargs)
        self.parent = parent
