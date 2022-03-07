from src.client.app_api import *
from src.client.utils.misc import connection, event_loop


class DialogFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super(DialogFrame, self).__init__(parent, **kwargs)
        self.configure(padding=0)

        style = ttk.Style()

        self.parent = parent
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
                                                      padding=5)

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

        event_loop.run_until_complete(connection.send_data(
            type=MESSAGE_NEW, data=message, dialog_name=self.dialog_name)
        )
        self.scrolled_text.text.delete(1.0, END)

    def recv_message(self):
        while True:
            message = connection.listen_server()
            print(message['data'])
            if len(message) > 0:
                if message['dialog_name'] == self.dialog_name:
                    print('YES')
                    message_frame_line = ttk.Frame(self.messages_frame.interior, bootstyle=INFO)
                    message_frame_line.pack(side=TOP, expand=TRUE, fill=X)

                    message_frame_line_label = ttk.Label(message_frame_line, text=message['data'])
                    message_frame_line_label.pack(side=LEFT, fill=BOTH)
            else:
                continue


if __name__ == '__main__':

    root = ttk.Window(title='Dialogue Frame', themename='superhero')
    DialogFrame(root).pack()
    root.mainloop()
