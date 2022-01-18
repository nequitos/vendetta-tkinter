from utils import *
from reg_frame import RegFrame
from recovery_frame import RecoveryFrame


class LoginFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super(LoginFrame, self).__init__(parent, **kwargs)

        self.parent = parent

        # form variables
        self.login = ttk.StringVar(value='')
        self.password = ttk.StringVar(value='')
        self.auto_auth = ttk.IntVar()

        self.create_form_entry('login:', self.login)
        self.create_form_entry('password:', self.password)

        self.create_button_box()

    def create_form_entry(self, label, variable):
        container = ttk.Frame(self)
        container.pack(fill=X, pady=5)

        lbl = ttk.Label(container, width=10, text=label.title())
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(container, width=50, textvariable=variable)
        ent.pack(side=LEFT, fill=X, padx=5)

    def create_button_box(self):
        container = ttk.Frame(self)
        container.pack(fill=X)

        auto_auth_btn = ttk.Checkbutton(
            container,
            text='auto authorization',
            variable=self.auto_auth)
        auto_auth_btn.pack(side=TOP)

        forgot_label = ttk.Label(
            container,
            bootstyle=INFO,
            text='Forgot password?',
            cursor='hand2'
        )
        forgot_label.bind('<Button-1>', self.on_forgot)
        forgot_label.pack(side=TOP)

        login_btn = ttk.Button(
            container,
            bootstyle=SECONDARY,
            width=10,
            text='login',
            takefocus=0,
            command=self.on_login
        )
        login_btn.pack(side=RIGHT, pady=15, padx=5)

        reg_btn = ttk.Button(
            container,
            bootstyle=SECONDARY,
            width=10,
            text='registration',
            takefocus=0,
            command=self.on_reg
        )
        reg_btn.pack(side=RIGHT, pady=15, padx=5)

    def on_forgot(self, event=None):
        self.pack_forget()
        RecoveryFrame(self.parent, self).pack()

    def on_login(self):
        pass

    def on_reg(self):
        self.pack_forget()
        RegFrame(self.parent, self).pack()


if __name__ == '__main__':
    from setup import theme

    root = ttk.Window(title='Login frame', themename=theme)
    LoginFrame(root).pack()
    root.mainloop()
