import customtkinter


class MyAccountWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('480x360')
        self.title('My Account')
        self.resizable(False, False)

        self.setup_widgets()

    def setup_widgets(self):
        # data will be taken from requests to db
        login = 'Crystal1s'
        self.login_label = customtkinter.CTkLabel(self, text=f'Hi, {login}!',
                                                  font=('arial', -24,))
        self.login_label.grid(row=0, column=1, pady=(10, 20))

        email = 'test@gmail.com'
        self.email = customtkinter.CTkLabel(self, text=f'Email: {email}')
        self.email.grid(row=1, column=0, padx=(20, 0))

        self.logout_btn = customtkinter.CTkButton(self, text='Log out',
                                                  command=self.logout,
                                                  width=40
                                                  )
        self.logout_btn.grid(row=2, column=2, sticky='es')

    def change_password(self):
        # change password func in future
        print('change password')

    def logout(self):
        # logout func in future
        print('Logout')
