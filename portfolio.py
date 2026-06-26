import json
import os
from datetime import datetime

PORTFOLIO_FILE = "portfolios.json"


class PortfolioManager:

    def __init__(self, username):

        self.username = username

        self.initialize_database()

    def initialize_database(self):

        if not os.path.exists(
                PORTFOLIO_FILE):

            with open(
                    PORTFOLIO_FILE,
                    "w") as file:

                json.dump(
                    {},
                    file,
                    indent=4
                )

    def load_portfolios(self):

        with open(
                PORTFOLIO_FILE,
                "r") as file:

            return json.load(file)

    def save_portfolios(
            self,
            portfolios
    ):

        with open(
                PORTFOLIO_FILE,
                "w") as file:

            json.dump(
                portfolios,
                file,
                indent=4
            )

    def create_user_portfolio(self):

        portfolios = \
            self.load_portfolios()

        if self.username \
                not in portfolios:

            portfolios[
                self.username
            ] = {

                "holdings": {},

                "watchlist": [],

                "created_at":
                str(datetime.now())

            }

            self.save_portfolios(
                portfolios
            )

    def buy_stock(
            self,
            stock,
            quantity,
            price
    ):

        portfolios = \
            self.load_portfolios()

        self.create_user_portfolio()

        user_data = \
            portfolios[
                self.username
            ]

        holdings = \
            user_data[
                "holdings"
            ]

        if stock in holdings:

            holdings[stock][
                "quantity"
            ] += quantity

        else:

            holdings[stock] = {

                "quantity":
                quantity,

                "buy_price":
                price,

                "purchase_date":
                str(
                    datetime.now()
                )

            }

        self.save_portfolios(
            portfolios
        )

        print(
            "Stock Purchased"
        )

    def sell_stock(
            self,
            stock,
            quantity
    ):

        portfolios = \
            self.load_portfolios()

        user_data = \
            portfolios[
                self.username
            ]

        holdings = \
            user_data[
                "holdings"
            ]

        if stock \
                not in holdings:

            print(
                "Stock Not Found"
            )

            return

        if quantity > \
                holdings[
                    stock
                ][
                    "quantity"
                ]:

            print(
                "Not Enough Shares"
            )

            return

        holdings[
            stock
        ][
            "quantity"
        ] -= quantity

        if holdings[
                stock
        ][
                "quantity"
        ] == 0:

            del holdings[
                stock
            ]

        self.save_portfolios(
            portfolios
        )

        print(
            "Stock Sold"
        )

    def view_holdings(self):

        portfolios = \
            self.load_portfolios()

        user_data = \
            portfolios.get(
                self.username,
                {}
            )

        holdings = \
            user_data.get(
                "holdings",
                {}
            )

        if not holdings:

            print(
                "No Holdings"
            )

            return

        print("\n")
        print("=" * 70)
        print("PORTFOLIO")
        print("=" * 70)

        for stock, data \
                in holdings.items():

            print(
                f"Stock : {stock}"
            )

            print(
                f"Quantity : "
                f"{data['quantity']}"
            )

            print(
                f"Buy Price : "
                f"{data['buy_price']}"
            )

            print(
                "-" * 70
            )

    def search_stock(
            self,
            stock
    ):

        portfolios = \
            self.load_portfolios()

        holdings = \
            portfolios[
                self.username
            ][
                "holdings"
            ]

        if stock \
                not in holdings:

            print(
                "Stock Not Found"
            )

            return

        data = \
            holdings[
                stock
            ]

        print("\n")
        print(
            "Stock Found"
        )

        print(
            "Quantity:",
            data["quantity"]
        )

        print(
            "Buy Price:",
            data["buy_price"]
        )

    def add_watchlist(
            self,
            stock
    ):

        portfolios = \
            self.load_portfolios()

        watchlist = \
            portfolios[
                self.username
            ][
                "watchlist"
            ]

        if stock \
                not in watchlist:

            watchlist.append(
                stock
            )

            self.save_portfolios(
                portfolios
            )

            print(
                "Added To Watchlist"
            )

    def view_watchlist(self):

        portfolios = \
            self.load_portfolios()

        watchlist = \
            portfolios[
                self.username
            ][
                "watchlist"
            ]

        print("\n")
        print(
            "=" * 50
        )

        print(
            "WATCHLIST"
        )

        print(
            "=" * 50
        )

        for stock in watchlist:

            print(
                stock
            )

    def portfolio_value(self):

        portfolios = \
            self.load_portfolios()

        holdings = \
            portfolios[
                self.username
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

        print(
            "\nPortfolio Value:",
            total
        )

        return total


def portfolio_menu(username):

    manager = \
        PortfolioManager(
            username
        )

    manager.create_user_portfolio()

    while True:

        print("\n")
        print("=" * 50)
        print("PORTFOLIO SYSTEM")
        print("=" * 50)

        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. View Holdings")
        print("4. Search Stock")
        print("5. Add Watchlist")
        print("6. View Watchlist")
        print("7. Portfolio Value")
        print("8. Exit")

        choice = input(
            "Choice: "
        )

        if choice == "1":

            stock = input(
                "Stock: "
            ).upper()

            qty = int(
                input(
                    "Quantity: "
                )
            )

            price = float(
                input(
                    "Price: "
                )
            )

            manager.buy_stock(
                stock,
                qty,
                price
            )

        elif choice == "2":

            stock = input(
                "Stock: "
            ).upper()

            qty = int(
                input(
                    "Quantity: "
                )
            )

            manager.sell_stock(
                stock,
                qty
            )

        elif choice == "3":

            manager.view_holdings()

        elif choice == "4":

            stock = input(
                "Search: "
            ).upper()

            manager.search_stock(
                stock
            )

        elif choice == "5":

            stock = input(
                "Stock: "
            ).upper()

            manager.add_watchlist(
                stock
            )

        elif choice == "6":

            manager.view_watchlist()

        elif choice == "7":

            manager.portfolio_value()

        elif choice == "8":

            break

        else:

            print(
                "Invalid Choice"
            )