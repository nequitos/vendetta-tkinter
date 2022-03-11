from ttkbootstrap.constants import *
import ttkbootstrap as ttk


class ScrolledFrame(ttk.Frame):
    """
    Implements a truly working frame for scrolling with a scroll bar.
    To embed any widget in this frame, use interior as the master argument.
    """

    def __init__(self, parent, **kwargs):
        super(ScrolledFrame, self).__init__(parent, **kwargs)
        self.bind('<Configure>', self._get_event_bind)
        self.configure(padding=0)
        self.parent = parent

        self.canvas = canvas = ttk.Canvas(self)
        self.canvas.pack(side=LEFT, expand=TRUE, fill=BOTH)

        self.scrollbar = scrollbar = ttk.Scrollbar(self, orient=VERTICAL,
                                                   command=canvas.yview)
        self.canvas.config(yscrollcommand=scrollbar.set)

        self.interior = interior = ttk.Frame(canvas)
        self.interior.bind('<Configure>', self._get_event_bind)
        self.interior_id = canvas.create_window((0, 0), window=interior, anchor=NW)

        self.update_idletasks()

    def _get_event_bind(self, event):
        self._set_scrollbar()
        self._update_frame_width()

    def _update_frame_width(self):
        self.canvas.itemconfig(self.interior_id, width=self.canvas.winfo_width())

    def _set_scrollbar(self):
        if self.interior.winfo_height() > self.parent.winfo_height():
            self.canvas.config(scrollregion=self.canvas.bbox(ALL))
            self.canvas.bind_all('<MouseWheel>', self._on_mousewheel)
            self.scrollbar.pack(side=RIGHT, fill=Y)
        else:
            self.canvas.config(scrollregion=(0, 0, 0, 0))
            self.scrollbar.pack_forget()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), 'units')


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