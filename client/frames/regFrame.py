from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from client.app_api.constants import *

from threading import Thread


class RegFrame(ttk.Frame):
    def __init__(self, parent, previous, connection, **kwargs):
        super(RegFrame, self).__init__(parent, **kwargs)

        self.parent = parent
        self.previous = previous
        self.connection = connection

        # form variables
        self.mail = ttk.StringVar(value='')
        self.name = ttk.StringVar(value='')
        self.password = ttk.StringVar(value='')
        self.re_password = ttk.StringVar(value='')
        self.invitation = ttk.StringVar(value='')
        self.code = ttk.StringVar(value='')

        # Head
        ttk.Label(self, text='Fill in the following information if you are creating an account').pack(side=TOP, pady=5)

        # creating
        mail_head = 'Enter your future mail'
        self.create_form_entry(mail_head, 'mail', self.mail)

        name_head = 'Enter your future name'
        self.create_form_entry(name_head, 'name', self.name)

        password_head = 'Enter your future password'
        self.create_form_entry(password_head, 'password', self.name)

        re_password_head = 'Repeat the password you entered'
        self.create_form_entry(re_password_head, 're-password', self.re_password)

        invitation_head = 'Enter the invitation code received by you or issued by someone else'
        self.create_form_entry(invitation_head, 'invitation', self.invitation)

        code_head = 'Code sent to your email'
        self.create_form_entry(code_head, 'code', self.code)

        self.create_button_box()

    def create_form_entry(self, head, label, variable):
        container = ttk.Frame(self)
        container.pack(fill=X, pady=5)

        ttk.Label(container, text=head).pack(side=TOP, fill=X)

        lbl = ttk.Label(container, width=15, text=label.title())
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(container, width=45, textvariable=variable)
        ent.pack(side=LEFT, fill=X, padx=5)

    def create_button_box(self):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=TRUE)

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
        send_btn.pack(side=RIGHT, pady=25, padx=5)

        cancel_btn = ttk.Button(
            container,
            width=10,
            text='cancel',
            takefocus=0,
            command=self.on_cancel
        )
        cancel_btn.pack(side=RIGHT, pady=25, padx=5)

    def on_send_code(self, label, event=None):
        label.configure(bootstyle=SECONDARY, cursor='arrow')
        Thread(
            target=self.connection.send_data,
            kwargs={'type': RECEIVE_REGISTRATION_CODE}
        )

    def on_send(self):
        pass

    def on_cancel(self):
        self.pack_forget()
        self.previous.pack()


if __name__ == '__main__':
    from client.utils.misc.connection import connection
    from loginFrame import LoginFrame

    root = ttk.Window(title='Registration frame')
    RegFrame(root, LoginFrame(root, connection=connection), connection=connection).pack()
    root.mainloop()