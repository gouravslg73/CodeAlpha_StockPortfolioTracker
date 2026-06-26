import csv
import json
import os
from datetime import datetime

PORTFOLIO_FILE = "portfolios.json"
REPORT_FILE = "portfolio_report.csv"


class ReportGenerator:

    def __init__(self):
        pass

    def load_data(self):

        if not os.path.exists(PORTFOLIO_FILE):
            return {}

        with open(PORTFOLIO_FILE, "r") as file:
            return json.load(file)

    def generate_csv_report(self, username):

        data = self.load_data()

        if username not in data:
            print("No portfolio found.")
            return

        portfolio = data[username]

        with open(REPORT_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Stock",
                "Quantity",
                "Buy Price",
                "Investment"
            ])

            total = 0

            for stock in portfolio:

                writer.writerow([
                    stock["stock"],
                    stock["quantity"],
                    stock["buy_price"],
                    stock["investment"]
                ])

                total += stock["investment"]

            writer.writerow([])

            writer.writerow([
                "Total Investment",
                total
            ])

        print("\nCSV Report Generated Successfully.")

    def generate_text_report(self, username):

        data = self.load_data()

        if username not in data:
            print("No portfolio found.")
            return

        filename = f"{username}_report.txt"

        with open(filename, "w") as file:

            file.write("=" * 50 + "\n")
            file.write("STOCK PORTFOLIO REPORT\n")
            file.write("=" * 50 + "\n\n")

            file.write(
                "Generated On : "
                + str(datetime.now())
                + "\n\n"
            )

            total = 0

            for stock in data[username]:

                file.write(
                    f"Stock : {stock['stock']}\n"
                )

                file.write(
                    f"Quantity : {stock['quantity']}\n"
                )

                file.write(
                    f"Buy Price : {stock['buy_price']}\n"
                )

                file.write(
                    f"Investment : {stock['investment']}\n"
                )

                file.write("-" * 40 + "\n")

                total += stock["investment"]

            file.write("\n")

            file.write(
                f"Total Investment : {total}\n"
            )

        print("Text Report Generated Successfully.")

    def show_summary(self, username):

        data = self.load_data()

        if username not in data:
            print("No portfolio found.")
            return

        portfolio = data[username]

        print("\n========== SUMMARY ==========")

        print("Total Stocks :", len(portfolio))

        total = 0

        for stock in portfolio:

            total += stock["investment"]

        print("Total Investment :", total)

        print("=============================")


if __name__ == "__main__":

    report = ReportGenerator()

    user = input("Enter Username : ")

    report.show_summary(user)

    report.generate_csv_report(user)

    report.generate_text_report(user)