from ttkbootstrap.constants import *
import ttkbootstrap as ttk


class ScrolledText(ttk.Frame):
    """
    New implementation of scrolling text based on ttkbootstrap.

    """

    def __init__(self, parent, **kwargs):
        super(ScrolledText, self).__init__(parent, **kwargs)

        self.configure(padding=0)
        self.parent = parent

        self.text = text = ttk.Text(self)
        self.text.pack(side=LEFT, expand=TRUE, fill=BOTH)

        self.scrollbar = scrollbar = ttk.Scrollbar(self, command=text.yview)
        self.text.config(yscrollcommand=scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
