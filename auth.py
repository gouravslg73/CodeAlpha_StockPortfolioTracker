import json
import os
import hashlib
from datetime import datetime

USERS_FILE = "users.json"


class UserDatabase:

    def __init__(self):
        self.initialize_database()

    def initialize_database(self):

        if not os.path.exists(USERS_FILE):

            with open(USERS_FILE, "w") as file:

                json.dump({}, file, indent=4)

    def load_users(self):

        try:

            with open(USERS_FILE, "r") as file:

                return json.load(file)

        except:

            return {}

    def save_users(self, users):

        with open(USERS_FILE, "w") as file:

            json.dump(users, file, indent=4)

    def hash_password(self, password):

        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    def user_exists(self, username):

        users = self.load_users()

        return username in users

    def register_user(
            self,
            username,
            password,
            email
    ):

        users = self.load_users()

        if username in users:

            return False

        users[username] = {

            "password":
            self.hash_password(password),

            "email":
            email,

            "created_at":
            str(datetime.now()),

            "last_login":
            "",

            "portfolio_value":
            0,

            "total_profit":
            0
        }

        self.save_users(users)

        return True

    def login_user(
            self,
            username,
            password
    ):

        users = self.load_users()

        if username not in users:

            return False

        hashed_password = self.hash_password(
            password
        )

        if users[username]["password"] \
                != hashed_password:

            return False

        users[username]["last_login"] = \
            str(datetime.now())

        self.save_users(users)

        return True

    def get_user_data(
            self,
            username
    ):

        users = self.load_users()

        return users.get(
            username,
            None
        )

    def update_portfolio_value(
            self,
            username,
            value
    ):

        users = self.load_users()

        if username in users:

            users[username][
                "portfolio_value"
            ] = value

            self.save_users(users)

    def update_profit(
            self,
            username,
            profit
    ):

        users = self.load_users()

        if username in users:

            users[username][
                "total_profit"
            ] = profit

            self.save_users(users)


class AuthenticationSystem:

    def __init__(self):

        self.db = UserDatabase()

    def register(self):

        print("\n")
        print("=" * 50)
        print("USER REGISTRATION")
        print("=" * 50)

        username = input(
            "Enter Username: "
        )

        if self.db.user_exists(
                username):

            print(
                "Username Already Exists"
            )

            return

        email = input(
            "Enter Email: "
        )

        password = input(
            "Enter Password: "
        )

        confirm = input(
            "Confirm Password: "
        )

        if password != confirm:

            print(
                "Passwords Do Not Match"
            )

            return

        if len(password) < 6:

            print(
                "Password Too Short"
            )

            return

        success = self.db.register_user(
            username,
            password,
            email
        )

        if success:

            print(
                "Registration Successful"
            )

        else:

            print(
                "Registration Failed"
            )

    def login(self):

        print("\n")
        print("=" * 50)
        print("USER LOGIN")
        print("=" * 50)

        username = input(
            "Username: "
        )

        password = input(
            "Password: "
        )

        success = self.db.login_user(
            username,
            password
        )

        if success:

            print(
                "Login Successful"
            )

            return username

        print(
            "Invalid Credentials"
        )

        return None

    def show_profile(
            self,
            username
    ):

        data = self.db.get_user_data(
            username
        )

        if not data:

            print(
                "User Not Found"
            )

            return

        print("\n")
        print("=" * 50)
        print("PROFILE")
        print("=" * 50)

        print(
            "Username:",
            username
        )

        print(
            "Email:",
            data["email"]
        )

        print(
            "Created:",
            data["created_at"]
        )

        print(
            "Last Login:",
            data["last_login"]
        )

        print(
            "Portfolio Value:",
            data["portfolio_value"]
        )

        print(
            "Total Profit:",
            data["total_profit"]
        )


def authentication_menu():

    auth = AuthenticationSystem()

    while True:

        print("\n")
        print("=" * 50)
        print("AUTHENTICATION SYSTEM")
        print("=" * 50)

        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input(
            "Enter Choice: "
        )

        if choice == "1":

            auth.register()

        elif choice == "2":

            user = auth.login()

            if user:

                return user

        elif choice == "3":

            return None

        else:

            print(
                "Invalid Choice"
            )


if __name__ == "__main__":

    logged_user = \
        authentication_menu()

    if logged_user:

        print(
            "Welcome",
            logged_user
        )