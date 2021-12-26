from utils import *


class MessagesFrame(ScrolledFrame):
    def __init__(self, parent, **kwargs):
        super(MessagesFrame, self).__init__(parent, **kwargs)
        self.configure(padding=0)

        self.style = ttk.Style()
        self.style.configure('secondary.TButtons', borderwidth=0)

        self.parent = parent
