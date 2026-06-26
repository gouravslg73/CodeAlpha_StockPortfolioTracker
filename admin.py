import json
import os
from datetime import datetime

USERS_FILE = "users.json"
PORTFOLIO_FILE = "portfolios.json"
LOG_FILE = "audit_log.txt"


class AdminPanel:

    def __init__(self):

        self.admin_username = "admin"
        self.admin_password = "admin123"

    def write_log(self, action):

        with open(
                LOG_FILE,
                "a") as file:

            file.write(
                f"{datetime.now()} | "
                f"{action}\n"
            )

    def load_users(self):

        if not os.path.exists(
                USERS_FILE):

            return {}

        with open(
                USERS_FILE,
                "r") as file:

            return json.load(file)

    def load_portfolios(self):

        if not os.path.exists(
                PORTFOLIO_FILE):

            return {}

        with open(
                PORTFOLIO_FILE,
                "r") as file:

            return json.load(file)

    def admin_login(self):

        username = input(
            "Admin Username: "
        )

        password = input(
            "Admin Password: "
        )

        if (
            username ==
            self.admin_username
            and
            password ==
            self.admin_password
        ):

            self.write_log(
                "Admin Login"
            )

            print(
                "Login Success"
            )

            return True

        print(
            "Invalid Admin Credentials"
        )

        return False

    def view_users(self):

        users = self.load_users()

        print("\n")
        print("=" * 60)
        print("ALL USERS")
        print("=" * 60)

        for user in users:

            print(user)

        self.write_log(
            "Viewed Users"
        )

    def delete_user(self):

        users = self.load_users()

        username = input(
            "Username To Delete: "
        )

        if username not in users:

            print(
                "User Not Found"
            )

            return

        del users[username]

        with open(
                USERS_FILE,
                "w") as file:

            json.dump(
                users,
                file,
                indent=4
            )

        self.write_log(
            f"Deleted User "
            f"{username}"
        )

        print(
            "User Deleted"
        )

    def system_stats(self):

        users = self.load_users()

        portfolios = \
            self.load_portfolios()

        print("\n")
        print("=" * 60)
        print("SYSTEM STATS")
        print("=" * 60)

        print(
            "Total Users:",
            len(users)
        )

        print(
            "Portfolios:",
            len(portfolios)
        )

        self.write_log(
            "Viewed Stats"
        )

    def leaderboard(self):

        portfolios = \
            self.load_portfolios()

        ranking = []

        for user in portfolios:

            holdings = \
                portfolios[
                    user
                ][
                    "holdings"
                ]

            total = 0

            for stock in holdings:

                total += (

                    holdings[
                        stock
                    ][
                        "quantity"
                    ]

                    *

                    holdings[
                        stock
                    ][
                        "buy_price"
                    ]
                )

            ranking.append(
                (
                    user,
                    total
                )
            )

        ranking.sort(
            key=lambda x: x[1],
            reverse=True
        )

        print("\n")
        print("=" * 60)
        print("LEADERBOARD")
        print("=" * 60)

        rank = 1

        for user, value in ranking:

            print(
                f"{rank}. "
                f"{user} "
                f"₹{value}"
            )

            rank += 1

        self.write_log(
            "Viewed Leaderboard"
        )

    def send_notification(self):

        message = input(
            "Notification Message: "
        )

        print("\n")
        print(
            "Notification Sent"
        )

        print(
            message
        )

        self.write_log(
            f"Notification: "
            f"{message}"
        )

    def audit_logs(self):

        if not os.path.exists(
                LOG_FILE):

            print(
                "No Logs Found"
            )

            return

        print("\n")
        print("=" * 60)
        print("AUDIT LOGS")
        print("=" * 60)

        with open(
                LOG_FILE,
                "r") as file:

            for line in file:

                print(
                    line.strip()
                )


def admin_menu():

    admin = AdminPanel()

    if not admin.admin_login():

        return

    while True:

        print("\n")
        print("=" * 50)
        print("ADMIN PANEL")
        print("=" * 50)

        print("1. View Users")
        print("2. Delete User")
        print("3. Leaderboard")
        print("4. System Stats")
        print("5. Send Notification")
        print("6. Audit Logs")
        print("7. Exit")

        choice = input(
            "Choice: "
        )

        if choice == "1":

            admin.view_users()

        elif choice == "2":

            admin.delete_user()

        elif choice == "3":

            admin.leaderboard()

        elif choice == "4":

            admin.system_stats()

        elif choice == "5":

            admin.send_notification()

        elif choice == "6":

            admin.audit_logs()

        elif choice == "7":

            break

        else:

            print(
                "Invalid Choice"
            )


if __name__ == "__main__":

    admin_menu()