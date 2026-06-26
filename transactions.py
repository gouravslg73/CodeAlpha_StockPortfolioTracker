import json
import os
from datetime import datetime

TRANSACTION_FILE = "transactions.json"


class TransactionManager:

    def __init__(self, username):

        self.username = username

        self.initialize_database()

    def initialize_database(self):

        if not os.path.exists(
                TRANSACTION_FILE):

            with open(
                    TRANSACTION_FILE,
                    "w") as file:

                json.dump(
                    {},
                    file,
                    indent=4
                )

    def load_transactions(self):

        with open(
                TRANSACTION_FILE,
                "r") as file:

            return json.load(file)

    def save_transactions(
            self,
            data
    ):

        with open(
                TRANSACTION_FILE,
                "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )

    def create_user_history(self):

        data = self.load_transactions()

        if self.username not in data:

            data[self.username] = []

            self.save_transactions(
                data
            )

    def add_transaction(
            self,
            action,
            stock,
            quantity,
            price
    ):

        data = self.load_transactions()

        self.create_user_history()

        transaction = {

            "action": action,

            "stock": stock,

            "quantity": quantity,

            "price": price,

            "timestamp":
            str(
                datetime.now()
            )

        }

        data[self.username].append(
            transaction
        )

        self.save_transactions(
            data
        )

    def view_history(self):

        data = self.load_transactions()

        history = data.get(
            self.username,
            []
        )

        if not history:

            print(
                "No Transactions Found"
            )

            return

        print("\n")
        print("=" * 80)
        print("TRANSACTION HISTORY")
        print("=" * 80)

        for item in history:

            print(
                f"{item['timestamp']}"
            )

            print(
                f"Action : "
                f"{item['action']}"
            )

            print(
                f"Stock : "
                f"{item['stock']}"
            )

            print(
                f"Quantity : "
                f"{item['quantity']}"
            )

            print(
                f"Price : "
                f"{item['price']}"
            )

            print(
                "-" * 80
            )

    def total_investment(self):

        data = self.load_transactions()

        history = data.get(
            self.username,
            []
        )

        total = 0

        for item in history:

            if item["action"] == "BUY":

                total += (
                    item["quantity"]
                    *
                    item["price"]
                )

        return total

    def total_sales(self):

        data = self.load_transactions()

        history = data.get(
            self.username,
            []
        )

        total = 0

        for item in history:

            if item["action"] == "SELL":

                total += (
                    item["quantity"]
                    *
                    item["price"]
                )

        return total

    def profit_loss(self):

        invested = \
            self.total_investment()

        sold = \
            self.total_sales()

        profit = sold - invested

        print("\n")
        print("=" * 50)
        print("PROFIT / LOSS")
        print("=" * 50)

        print(
            "Total Invested:",
            invested
        )

        print(
            "Total Sold:",
            sold
        )

        print(
            "Profit/Loss:",
            profit
        )

        return profit

    def roi(self):

        invested = \
            self.total_investment()

        sold = \
            self.total_sales()

        if invested == 0:

            print(
                "No Investment Found"
            )

            return 0

        roi = (
            (
                sold -
                invested
            )
            /
            invested
        ) * 100

        print(
            "\nROI:",
            round(
                roi,
                2
            ),
            "%"
        )

        return roi

    def stock_performance(self):

        data = self.load_transactions()

        history = data.get(
            self.username,
            []
        )

        stock_profit = {}

        for item in history:

            stock = item["stock"]

            amount = (
                item["quantity"]
                *
                item["price"]
            )

            if stock not in stock_profit:

                stock_profit[
                    stock
                ] = 0

            if item["action"] == "BUY":

                stock_profit[
                    stock
                ] -= amount

            else:

                stock_profit[
                    stock
                ] += amount

        return stock_profit

    def top_gainer(self):

        performance = \
            self.stock_performance()

        if not performance:

            print(
                "No Data Available"
            )

            return

        best = max(
            performance,
            key=performance.get
        )

        print("\n")
        print(
            "TOP GAINER"
        )

        print(
            best,
            performance[best]
        )

    def top_loser(self):

        performance = \
            self.stock_performance()

        if not performance:

            print(
                "No Data Available"
            )

            return

        worst = min(
            performance,
            key=performance.get
        )

        print("\n")
        print(
            "TOP LOSER"
        )

        print(
            worst,
            performance[worst]
        )

    def analytics_dashboard(self):

        print("\n")
        print("=" * 60)
        print("PORTFOLIO ANALYTICS")
        print("=" * 60)

        self.profit_loss()

        self.roi()

        self.top_gainer()

        self.top_loser()


def transaction_menu(username):

    manager = \
        TransactionManager(
            username
        )

    manager.create_user_history()

    while True:

        print("\n")
        print("=" * 50)
        print("TRANSACTION MENU")
        print("=" * 50)

        print("1. View History")
        print("2. Profit/Loss")
        print("3. ROI")
        print("4. Top Gainer")
        print("5. Top Loser")
        print("6. Dashboard")
        print("7. Exit")

        choice = input(
            "Choice: "
        )

        if choice == "1":

            manager.view_history()

        elif choice == "2":

            manager.profit_loss()

        elif choice == "3":

            manager.roi()

        elif choice == "4":

            manager.top_gainer()

        elif choice == "5":

            manager.top_loser()

        elif choice == "6":

            manager.analytics_dashboard()

        elif choice == "7":

            break

        else:

            print(
                "Invalid Choice"
            )