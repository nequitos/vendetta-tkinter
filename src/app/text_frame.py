from utils import *


class TextFrame(ScrolledFrame):
    def __init__(self, parent, **kwargs):
        super(TextFrame, self).__init__(parent, **kwargs)
        self.configure(padding=0)

        self.style = ttk.Style()
        self.style.configure('secondary.TButtons', borderwidth=0)

        self.parent = parent

        self.text = ttk.Text(self.interior)
        self.text.pack(side=TOP, expand=TRUE, fill=BOTH)
