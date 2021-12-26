

from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from ttkbootstrap.dialogs import Dialog


class DialogFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super(DialogFrame, self).__init__(parent, **kwargs)
        self.configure(padding=0)

        style = ttk.Style()

        self.parent = parent

        # ----- Notebook
        self.notebook = notebook = ttk.Notebook(self)

        self.info_button = info_button = ttk.Button(notebook, bootstyle=SECONDARY,
                                                    text='View pinned.',
                                                    takefocus=0,
                                                    padding=5)
        self.voice_button = voice_button = ttk.Button(notebook, bootstyle=SECONDARY,
                                                      text='Record a voice message.',
                                                      takefocus=0,
                                                      padding=5)
        self.media_button = media_button = ttk.Button(notebook, bootstyle=SECONDARY,
                                                      takefocus=0,
                                                      text='Select media.',
                                                      padding=5)

        self.notebook.add(info_button, text='Info')
        self.notebook.add(voice_button, text='Voice')
        self.notebook.add(media_button, text='Media')

        self.notebook.pack(side=TOP, fill=X)

        # ----- Messages box
        messages_frame = ttk.Frame(self)
        messages_frame.pack(side=TOP, expand=TRUE, fill=BOTH, anchor=CENTER)

        self.m_canvas = m_canvas = ttk.Canvas(messages_frame)
        m_canvas.pack(side=LEFT, expand=TRUE, fill=BOTH, anchor=CENTER)

        self.m_scrollbar = m_scrollbar = ttk.Scrollbar(messages_frame, command=m_canvas.yview)
        m_canvas.config(yscrollcommand=m_scrollbar.set)

        self.m_interior = m_interior = ttk.Frame(m_canvas)
        m_canvas.create_window((0, 0), window=m_interior, anchor=NW)
        m_interior.bind('<Configure>', self._set_messages_frame_scrollbar)

        # ----- Control box
        control_frame = ttk.Frame(self)
        control_frame.pack(side=TOP, fill=BOTH, anchor=CENTER)

        c_send_btn = ttk.Button(control_frame,
                                text='send',
                                takefocus=0,
                                padding=0)
        c_send_btn.pack(side=RIGHT, fill=BOTH)

        # ----- Control text box
        self.control_text_frame = control_text_frame = ttk.Frame(control_frame)
        self.control_text_frame.pack(side=LEFT, expand=TRUE, fill=BOTH, anchor=CENTER)

        ct_canvas = ttk.Canvas(control_text_frame)
        ct_canvas.pack(side=LEFT, expand=TRUE, fill=BOTH, anchor=CENTER)

        ct_scrollbar = ttk.Scrollbar(control_text_frame, command=ct_canvas.yview)
        ct_canvas.config(yscrollcommand=ct_scrollbar.set)
        ct_scrollbar.pack(side=RIGHT, fill=Y, anchor=CENTER)

        c_text = ttk.Text(ct_canvas, height=3)
        c_text.pack(fill=BOTH)

        self.update_idletasks()

    def _set_messages_frame_scrollbar(self, event):
        if self.m_interior.winfo_height() > self.winfo_height():
            self.m_canvas.config(scrollregion=self.m_canvas.bbox(ALL))
            self.m_scrollbar.pack(side=RIGHT, fill=Y)
        else:
            self.m_canvas.config(scrollregion=(0, 0, 0, 0))
            self.m_scrollbar.pack_forget()

    def _set_ct_frame_scrollbar(self):
        # if self.control_text_frame.winfo_height() >
        pass

    def _send_message(self):
        message_line = None


if __name__ == '__main__':
    root = ttk.Window(title='Dialog Frame', themename='superhero')
    DialogFrame(root).pack(expand=TRUE, fill=BOTH)
    root.mainloop()