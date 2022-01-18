from utils import *


class LoginWindow(ttk.Window):
    def __init__(self, **kwargs):
        super(LoginWindow, self).__init__(**kwargs)
        self.resizable(FALSE, FALSE)
        self.geometry('400x200')

        # form variables
        self.login = ttk.StringVar(value='')
        self.password = ttk.StringVar(value='')

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
        container.pack(fill=X, expand=TRUE)

        auto_auth_btn = ttk.Checkbutton(
            container,
            text='auto authorization')
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
        login_btn.pack(side=RIGHT, pady=25, padx=5)

        reg_btn = ttk.Button(
            container,
            bootstyle=SECONDARY,
            width=10,
            text='registration',
            takefocus=0,
            command=self.on_reg
        )
        reg_btn.pack(side=RIGHT, pady=25, padx=5)

    def on_forgot(self, event):
        pass

    def on_login(self):
        pass

    def on_reg(self):
        pass


if __name__ == '__main__':
    from setup import theme

    LoginWindow(title='Login Window', themename=theme).mainloop()