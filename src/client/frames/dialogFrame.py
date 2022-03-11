from src.client.app_api import *
from src.client.utils.misc.connection import connection

from tkinter.filedialog import askopenfilename
from src.client.handlers.mediaHandler import MediaHandler


from PIL import Image, ImageTk


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
                                                      command=self.send_file)

        self.notebook.add(info_button, text='Info')
        self.notebook.add(voice_button, text='Voice')
        self.notebook.add(media_button, text='Media')

        self.notebook.pack(side=TOP, fill=X)

        # ----- Messages Frame
        self.messages_frame = ScrolledFrame(self)
        self.messages_frame.pack(side=TOP, expand=TRUE, fill=BOTH)

        # ----- Text Frame
        self.scrolled_text = ScrolledText(self)
        self.scrolled_text.text.config(height=3)
        self.scrolled_text.text.bind('<Return>', self.send_message)
        self.scrolled_text.pack(side=LEFT, expand=TRUE, fill=BOTH)

        # ----- Control Frame
        control_frame = ttk.Frame(self)
        control_frame.pack(side=RIGHT, expand=FALSE, fill=BOTH)

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

    def send_file(self):
        file = askopenfilename()
        image = ImageTk.PhotoImage(Image.open(file))

        with open(file, 'rb') as media_fl:
            media = media_fl.read()

        message_frame_line = ttk.Frame(self.messages_frame.interior, bootstyle=INFO)
        message_frame_line.pack(side=TOP, expand=TRUE, fill=X)

        message_frame_line_label = ttk.Label(message_frame_line, bootstyle=WARNING,
                                             cursor='hand2')
        message_frame_line_label.bind('<Button-1>', lambda _: MediaHandler(
            message_frame_line, message_frame_line_label, file
        ))
        message_frame_line_label.pack(side=RIGHT, fill=BOTH)

        MediaHandler(
            message_frame_line, message_frame_line_label, file
        )
        # Thread(
        #     target=self.connection.send_data,
        #     kwargs={'type': MEDIA_FILE, 'file': media, 'file_name': file_name}
        # ).start()

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
    root = ttk.Window(title='Dialogue Frame', themename='superhero')
    DialogFrame(root, connection=connection).pack()
    root.mainloop()
