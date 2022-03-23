from ttkbootstrap.constants import *
import ttkbootstrap as ttk


class XScrolledFrame(ttk.Frame):
    """
    Implements a really working scroll frame with a horizontal scrollbar.
    To embed any widget in this frame, use interior as the main argument.

    """

    def __init__(self, parent, **kwargs):
        super(XScrolledFrame, self).__init__(parent)
        self.bind('<Configure>', self._get_event_bind)
        self.configure(padding=0)
        self.parent = parent

        self.update_frame_width_mode = False
        self.update_frame_height_mode = False

        self.canvas = canvas = ttk.Canvas(self)
        self.canvas.pack(side=BOTTOM, expand=TRUE, fill=X)

        self.scrollbar = scrollbar = ttk.Scrollbar(self, orient=HORIZONTAL,
                                                   command=canvas.xview)
        self.canvas.config(xscrollcommand=scrollbar.set)

        self.interior = interior = ttk.Frame(canvas)
        self.interior.bind('<Configure>', self._get_event_bind)
        self.interior_id = canvas.create_window((0, 0), window=interior, anchor=NW)

        self.update_idletasks()

    def _get_event_bind(self, event):
        self._set_scrollbar()

        if self.update_frame_width_mode:
            self._update_frame_width()
        if self.update_frame_height_mode:
            self._update_frame_height()

    def _update_frame_width(self):
        self.canvas.itemconfig(self.interior_id, width=self.canvas.winfo_width())

    def _update_frame_height(self):
        self.canvas.itemconfig(self.interior_id, height=self.canvas.winfo_height())

    def _set_scrollbar(self):
        if self.interior.winfo_width() >= self.parent.winfo_width():
            self.canvas.config(scrollregion=self.canvas.bbox(ALL))
            self.canvas.bind_all('<MouseWheel>', self._on_mousewheel)
            self.scrollbar.pack(side=BOTTOM, fill=X)
        else:
            self.canvas.config(scrollregion=(0, 0, 0, 0))
            self.scrollbar.pack_forget()

    def _on_mousewheel(self, event):
        self.canvas.xview_scroll(int(-1 * (event.delta / 120)), 'units')
