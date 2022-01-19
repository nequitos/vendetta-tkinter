from setup import *


class RecoveryFrame(ttk.Frame):
    def __init__(self, parent, previous, **kwargs):
        super(RecoveryFrame, self).__init__(parent, **kwargs)

        self.parent = parent
        self.previous = previous

        # form variables
        self.mail = ttk.StringVar(value='')
        self.password = ttk.StringVar(value='')
        self.re_password = ttk.StringVar(value='')
        self.code = ttk.StringVar(value='')

        # Head
        ttk.Label(self, text='Enter the following details to recover your account').pack(side=TOP, pady=5)

        self.create_form_entry('Email specified during registration', 'mail', self.mail)
        self.create_form_entry('The new password you want to set', 'password', self.password)
        self.create_form_entry('Renew new password', 're-password', self.re_password)
        self.create_form_entry('Code sent to your email', 'code', self.code)

        self.create_button_box()

    def create_form_entry(self, head, label, variable):
        container = ttk.Frame(self)
        container.pack(fill=X)

        ttk.Label(container, text=head).pack(side=TOP, fill=X)

        lbl = ttk.Label(container, width=15, text=label.title())
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(container, width=45, textvariable=variable)
        ent.pack(side=LEFT, fill=X, padx=5)

    def create_button_box(self):
        container = ttk.Frame(self)
        container.pack(side=TOP, fill=X)

        send_code_label = ttk.Label(
            container,
            bootstyle=INFO,
            text='send code to email',
            cursor='hand2'
        )
        send_code_label.bind('<Button-1>', lambda _: self.on_send_code(send_code_label))
        send_code_label.pack(side=TOP, pady=10)

        send_btn = ttk.Button(
            container,
            width=10,
            text='send',
            takefocus=0,
            command=self.on_send
        )
        send_btn.pack(side=RIGHT, pady=15, padx=5)

        cancel_btn = ttk.Button(
            container,
            width=10,
            text='cancel',
            takefocus=0,
            command=self.on_cancel
        )
        cancel_btn.pack(side=RIGHT, pady=15, padx=5)

    def on_send_code(self, label, event=None):
        label.configure(bootstyle=SECONDARY, cursor='arrow')

    def on_send(self):
        pass

    def on_cancel(self):
        self.pack_forget()
        self.previous.pack()


if __name__ == '__main__':
    from setup import theme
    from login_frame import LoginFrame

    root = ttk.Window(title='Recovery frame', themename=theme)
    RecoveryFrame(root, LoginFrame(root)).pack()
    root.mainloop()
