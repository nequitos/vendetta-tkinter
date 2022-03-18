from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tkinter.filedialog import askopenfilename

from client.app_api.scrollbarWidgets import XScrolledFrame, YScrolledFrame, ScrolledText
from client.frames.bufferLabel import BufferLabel
from client.app_api.constants import *

from threading import Thread


class DialogFrame(ttk.Frame):
    def __init__(self, parent, connection, **kwargs):
        super(DialogFrame, self).__init__(parent, **kwargs)
        self.configure(padding=0)

        style = ttk.Style()

        self.parent = parent
        self.connection = connection
        self.dialog_name = None

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
                                                      padding=5,
                                                      command=self.insert_file)

        self.notebook.add(info_button, text='Info')
        self.notebook.add(voice_button, text='Voice')
        self.notebook.add(media_button, text='Media')

        self.notebook.pack(side=TOP, fill=X)

        # ----- Messages Frame
        self.messages_frame = YScrolledFrame(self)
        self.messages_frame.pack(side=TOP, expand=TRUE, fill=BOTH)

        # ----- Text Frame
        self.scrolled_text = ScrolledText(self)
        self.scrolled_text.text.config(height=2)
        self.scrolled_text.text.bind('<Return>', self.send_message)
        self.scrolled_text.pack(side=BOTTOM, expand=FALSE, fill=BOTH)

        # ----- Control Frame
        control_frame = ttk.Frame(self)
        control_frame.pack(side=RIGHT, expand=FALSE, fill=BOTH)

        # ----- Buffer Frame
        self.buffer_frame = XScrolledFrame(self, height=1)
        self.buffer_frame.canvas.config(height=60)
        self.buffer_frame.pack(side=BOTTOM, expand=FALSE, fill=BOTH)

        self.update_idletasks()
        Thread(target=self.recv_message).start()

    def send_message(self, event):
        message = self.scrolled_text.text.get(1.0, END).strip()

        message_frame_line = ttk.Frame(self.messages_frame.interior, bootstyle=INFO)
        message_frame_line.pack(side=TOP, expand=TRUE, fill=X)

        message_frame_line_label = ttk.Label(message_frame_line, text=message)
        message_frame_line_label.pack(side=RIGHT, fill=BOTH)

        Thread(
            target=self.connection.send_data,
            kwargs={'type': MESSAGE_NEW, 'data': message, 'dialog_name': self.dialog_name}
        ).start()

        self.scrolled_text.text.delete(1.0, END)

    def insert_file(self):
        file = askopenfilename()

        buffer_label = BufferLabel(self.buffer_frame.interior, file)
        buffer_label.pack(side=LEFT, fill=BOTH)

    def del_insert_file(self):
        pass

    def recv_message(self):
        while True:
            message = self.connection.listen_server()
            if len(message) > 0:
                if message['dialog_name'] == self.dialog_name:
                    message_frame_line = ttk.Frame(self.messages_frame.interior, bootstyle=INFO)
                    message_frame_line.pack(side=TOP, expand=TRUE, fill=X)

                    message_frame_line_label = ttk.Label(message_frame_line, text=message['data'])
                    message_frame_line_label.pack(side=LEFT, fill=BOTH)
            else:
                continue


if __name__ == '__main__':
    from client.utils.misc.connection import connection

    root = ttk.Window(title='Dialogue Frame', themename='superhero')
    DialogFrame(root, connection=connection).pack()
    root.mainloop()
