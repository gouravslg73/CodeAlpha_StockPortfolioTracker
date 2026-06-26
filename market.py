import json
import csv
import shutil
import os
from datetime import datetime
import matplotlib.pyplot as plt


class ReportManager:

    def __init__(self,
                 username,
                 portfolio_file):

        self.username = username
        self.portfolio_file = portfolio_file

    def load_data(self):

        with open(
                self.portfolio_file,
                "r") as file:

            return json.load(file)

    def get_holdings(self):

        data = self.load_data()

        return data[
            self.username
        ][
            "holdings"
        ]

    def export_csv(self):

        holdings = self.get_holdings()

        filename = (
            f"{self.username}"
            "_portfolio.csv"
        )

        with open(
                filename,
                "w",
                newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Stock",
                "Quantity",
                "Buy Price",
                "Value"
            ])

            for stock, data \
                    in holdings.items():

                value = (
                    data["quantity"]
                    *
                    data["buy_price"]
                )

                writer.writerow([
                    stock,
                    data["quantity"],
                    data["buy_price"],
                    value
                ])

        print(
            "CSV Exported"
        )

    def export_text_report(self):

        holdings = self.get_holdings()

        filename = (
            f"{self.username}"
            "_report.txt"
        )

        with open(
                filename,
                "w"
        ) as file:

            file.write(
                "PORTFOLIO REPORT\n"
            )

            file.write(
                "=" * 50
            )

            file.write("\n")

            for stock, data \
                    in holdings.items():

                file.write(
                    f"{stock}\n"
                )

                file.write(
                    f"Qty: "
                    f"{data['quantity']}\n"
                )

                file.write(
                    f"Price: "
                    f"{data['buy_price']}\n"
                )

                file.write(
                    "\n"
                )

        print(
            "Text Report Saved"
        )

    def portfolio_dashboard(self):

        holdings = self.get_holdings()

        total_value = 0

        total_stocks = len(
            holdings
        )

        for stock in holdings:

            total_value += (

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

        print("\n")
        print("=" * 60)
        print("DASHBOARD")
        print("=" * 60)

        print(
            "User:",
            self.username
        )

        print(
            "Total Stocks:",
            total_stocks
        )

        print(
            "Portfolio Value:",
            total_value
        )

        print(
            "Generated:",
            datetime.now()
        )

    def backup_data(self):

        backup_name = (

            "backup_"

            +

            datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            +

            ".json"
        )

        shutil.copy(
            self.portfolio_file,
            backup_name
        )

        print(
            "Backup Created:"
        )

        print(
            backup_name
        )

    def restore_backup(self):

        backup_file = input(
            "Backup Filename: "
        )

        if not os.path.exists(
                backup_file):

            print(
                "Backup Not Found"
            )

            return

        shutil.copy(
            backup_file,
            self.portfolio_file
        )

        print(
            "Backup Restored"
        )

    def pie_chart(self):

        holdings = self.get_holdings()

        labels = []
        values = []

        for stock, data \
                in holdings.items():

            labels.append(
                stock
            )

            values.append(
                data["quantity"]
                *
                data["buy_price"]
            )

        plt.figure(
            figsize=(8, 8)
        )

        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%"
        )

        plt.title(
            "Portfolio Distribution"
        )

        plt.show()

    def bar_chart(self):

        holdings = self.get_holdings()

        stocks = []
        values = []

        for stock, data \
                in holdings.items():

            stocks.append(
                stock
            )

            values.append(
                data["quantity"]
                *
                data["buy_price"]
            )

        plt.figure(
            figsize=(10, 5)
        )

        plt.bar(
            stocks,
            values
        )

        plt.title(
            "Portfolio Value"
        )

        plt.xlabel(
            "Stocks"
        )

        plt.ylabel(
            "Investment"
        )

        plt.show()

    def summary_report(self):

        self.portfolio_dashboard()

        self.export_csv()

        self.export_text_report()

        print(
            "\nSummary Generated"
        )


def report_menu(username):

    report = ReportManager(
        username,
        "portfolios.json"
    )

    while True:

        print("\n")
        print("=" * 50)
        print("REPORT CENTER")
        print("=" * 50)

        print("1. Dashboard")
        print("2. Export CSV")
        print("3. Export TXT")
        print("4. Pie Chart")
        print("5. Bar Chart")
        print("6. Backup Data")
        print("7. Restore Data")
        print("8. Summary Report")
        print("9. Exit")

        choice = input(
            "Choice: "
        )

        if choice == "1":

            report.portfolio_dashboard()

        elif choice == "2":

            report.export_csv()

        elif choice == "3":

            report.export_text_report()

        elif choice == "4":

            report.pie_chart()

        elif choice == "5":

            report.bar_chart()

        elif choice == "6":

            report.backup_data()

        elif choice == "7":

            report.restore_backup()

        elif choice == "8":

            report.summary_report()

        elif choice == "9":

            break

        else:

            print(
                "Invalid Choice"
            )