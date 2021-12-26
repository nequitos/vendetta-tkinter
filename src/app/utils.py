from ttkbootstrap.constants import *
import ttkbootstrap as ttk


class ScrolledFrame(ttk.Frame):
    """
    Implements a truly working frame for scrolling with a scroll bar.
    To embed any widget in this frame, use interior as the master argument.
    """

    def __init__(self, parent, **kwargs):
        super(ScrolledFrame, self).__init__(parent, **kwargs)
        self.bind('<Configure>', self._set_scrollbar)
        self.configure(padding=0)
        self.parent = parent

        self.canvas = canvas = ttk.Canvas(self)
        self.canvas.pack(side=LEFT, expand=TRUE, fill=BOTH)

        self.scrollbar = scrollbar = ttk.Scrollbar(self, orient=VERTICAL,
                                                   command=canvas.yview)
        self.canvas.config(yscrollcommand=scrollbar.set)

        self.interior = interior = ttk.Frame(canvas)
        self.interior.bind('<Configure>', self._set_scrollbar)
        self.canvas.create_window((0, 0), window=interior, anchor=NW)

        self.update_idletasks()

    def _set_scrollbar(self, event):
        if self.interior.winfo_height() > self.parent.winfo_height():
            self.canvas.config(scrollregion=self.canvas.bbox(ALL))
            self.scrollbar.pack(side=RIGHT, fill=Y)
        else:
            self.canvas.config(scrollregion=(0, 0, 0, 0))
            self.scrollbar.pack_forget()


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
