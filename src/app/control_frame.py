from utils import *


class ControlFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super(ControlFrame, self).__init__(parent, **kwargs)
        self.configure(padding=0)

        self.style = ttk.Style()
        self.style.configure('secondary.TButton', borderwidth=0)

        self.parent = parent

        self.send_btn = ttk.Button(self, bootstyle=SECONDARY,
                                   text='send',
                                   takefocus=0,
                                   padding=0)
        self.send_btn.pack(side=LEFT, fill=BOTH)
