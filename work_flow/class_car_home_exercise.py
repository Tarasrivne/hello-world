class User():
    def __init__(self, first_name, last_name, year):
        self.first_name = first_name
        self.last_name = last_name
        self.mid_name = ''
        self.year = year
        self.login_attempts = 0

    def describe_user(self):
        all_information = f"{self.first_name} {self.last_name} {self.year}"
        print(all_information.title())


    def great_user(self):
        print(f"hello {self.first_name} {self.last_name}".title())

    def increment_login_attempts(self, login):
        self.login_attempts = login
        if login >= 1 and login <= 9:
            print(f" login attempts {self.login_attempts}")
        else:
            login == 0
            print("razing has been reset, login attempts = 0 ")

    def reset_login_attempts(self):
        print(self.login_attempts == 0)

user_view = User('Taras', 'Viktorchuk', 33)
anozer_user = User('Nik', 'von', 30)
anozer_user.great_user()
user_view.describe_user()
user_view.great_user()
user_view.increment_login_attempts(13)
user_view.reset_login_attempts()