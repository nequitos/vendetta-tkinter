from utils import *


class LoginWindow(ttk.Window):
    def __init__(self, **kwargs):
        super(LoginWindow, self).__init__(**kwargs)
        self.resizable(FALSE, FALSE)
        self.geometry('400x200')

        self.grid_columnconfigure(0, minsize=100)
        self.grid_columnconfigure(1, minsize=100)
        self.grid_columnconfigure(2, minsize=100)
        self.grid_columnconfigure(3, minsize=100)
        self.grid_columnconfigure(4, minsize=100)

        ttk.Label(text='Login:').grid(row=0, column=0, padx=10, pady=10, sticky=W)
        ttk.Label(text='Password:').grid(row=1, column=0, padx=10, pady=10, sticky=W)

        login_entry = ttk.Entry()
        login_entry.grid(row=0, column=1, columnspan=3, sticky=W+E)

        password_entry = ttk.Entry()
        password_entry.grid(row=1, column=1, columnspan=3, sticky=W+E)

        auto_login_check_btn = ttk.Checkbutton(text='auto login')
        auto_login_check_btn.grid(row=2, column=1, columnspan=2, sticky=N, pady=5)

        forgot_password_label = ttk.Label(bootstyle=INFO,
                                          text='Forgot password?',
                                          justify=CENTER,
                                          cursor='hand2')
        forgot_password_label.bind('<Button-1>', self.password_recovery)
        forgot_password_label.grid(row=3, column=1, columnspan=2, sticky=N)

        registration_btn = ttk.Button(bootstyle=SECONDARY,
                                      text='registration',
                                      takefocus=0,
                                      command=self.registration)
        registration_btn.grid(row=4, column=2, sticky=W+E, pady=20)

        login_btn = ttk.Button(bootstyle=SECONDARY,
                               text='login',
                               takefocus=0)
        login_btn.grid(row=4, column=3, sticky=W+E)

        self.update_idletasks()

    @staticmethod
    def registration():
        registration_window = ttk.Toplevel(title='Create an account for Vendetta')
        registration_window.resizable(FALSE, FALSE)
        registration_window.geometry('390x350')

        registration_window.grid_columnconfigure(0, minsize=70)
        registration_window.grid_columnconfigure(1, minsize=70)

        ttk.Label(registration_window,
                  text='Enter your email').grid(row=0, column=0, columnspan=3, sticky=N, pady=10)

        ttk.Label(registration_window,
                  text='Mail:').grid(row=1, column=0, sticky=W, padx=10)
        mail_entry = ttk.Entry(registration_window)
        mail_entry.grid(row=1, column=1, columnspan=2, sticky=W+E)

    @staticmethod
    def password_recovery(event):
        recovery_window = ttk.Toplevel(title='Vendetta account recovery')
        recovery_window.resizable(FALSE, FALSE)
        recovery_window.geometry('390x150')

        recovery_window.grid_columnconfigure(0, minsize=130)
        recovery_window.grid_columnconfigure(1, minsize=130)
        recovery_window.grid_columnconfigure(2, minsize=130)

        ttk.Label(recovery_window,
                  text='Enter the email to which the account is linked',
                  justify=CENTER).grid(row=0, column=0, columnspan=3, sticky=N, pady=10)

        ttk.Label(recovery_window, text='Mail:').grid(row=1, column=0, sticky=N)
        recovery_mail_entry = ttk.Entry(recovery_window)
        recovery_mail_entry.grid(row=1, column=1, columnspan=3, sticky=W+E)

        ttk.Button(recovery_window, bootstyle=SECONDARY,
                   text='send',
                   takefocus=0).grid(row=2, column=0, columnspan=3, sticky=W+E, pady=30)

        recovery_window.mainloop()


if __name__ == '__main__':
    from setup import theme

    LoginWindow(title='Login Window', themename=theme).mainloop()