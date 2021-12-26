from messages_frame import MessagesFrame
from control_frame import ControlFrame

from utils import *


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

        # ----- Messages Frame
        messages_frame = MessagesFrame(self)
        messages_frame.pack(side=TOP, expand=TRUE, fill=BOTH)

        # ----- Text Frame
        text = ScrolledText(self)
        text.text.config(height=3)
        text.pack(side=LEFT, expand=TRUE, fill=BOTH)

        # ----- Control Frame
        control_frame = ControlFrame(self)
        control_frame.pack(side=RIGHT, expand=FALSE, fill=BOTH)

        self.update_idletasks()


if __name__ == '__main__':
    root = ttk.Window(title='Dialog Frame', themename='superhero')
    DialogFrame(root).pack(expand=TRUE, fill=BOTH)
    root.mainloop()
