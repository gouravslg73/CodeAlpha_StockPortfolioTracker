import json
from datetime import datetime


class AdvancedAnalytics:

    def __init__(
            self,
            portfolio_file,
            username
    ):

        self.portfolio_file = \
            portfolio_file

        self.username = username

        self.sector_mapping = {

            "AAPL":
            "Technology",

            "GOOGL":
            "Technology",

            "MSFT":
            "Technology",

            "TSLA":
            "Automobile",

            "TATA":
            "Industrial",

            "NANO":
            "Industrial",

            "AMZN":
            "Ecommerce",

            "NFLX":
            "Entertainment"
        }

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

    def diversification_report(self):

        holdings = \
            self.get_holdings()

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

        print("\n")
        print("=" * 60)
        print(
            "DIVERSIFICATION REPORT"
        )
        print("=" * 60)

        for stock in holdings:

            value = (
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

            percentage = (
                value /
                total
            ) * 100

            print(
                f"{stock:<10}"
                f"{percentage:.2f}%"
            )

    def sector_allocation(self):

        holdings = \
            self.get_holdings()

        sectors = {}

        for stock in holdings:

            sector = \
                self.sector_mapping.get(
                    stock,
                    "Other"
                )

            value = (
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

            sectors[
                sector
            ] = sectors.get(
                sector,
                0
            ) + value

        print("\n")
        print("=" * 60)
        print(
            "SECTOR ALLOCATION"
        )
        print("=" * 60)

        for sector, value \
                in sectors.items():

            print(
                f"{sector:<20}"
                f"₹{value}"
            )

    def risk_analysis(self):

        holdings = \
            self.get_holdings()

        total_stocks = \
            len(holdings)

        print("\n")
        print("=" * 60)
        print("RISK ANALYSIS")
        print("=" * 60)

        if total_stocks <= 2:

            print(
                "High Risk Portfolio"
            )

        elif total_stocks <= 5:

            print(
                "Medium Risk Portfolio"
            )

        else:

            print(
                "Low Risk Portfolio"
            )

    def investment_score(self):

        holdings = \
            self.get_holdings()

        score = 50

        stock_count = \
            len(holdings)

        if stock_count >= 5:

            score += 20

        if stock_count >= 10:

            score += 20

        if stock_count >= 15:

            score += 10

        print("\n")
        print("=" * 60)
        print(
            "INVESTMENT SCORE"
        )
        print("=" * 60)

        print(
            "Score:",
            score,
            "/100"
        )

        return score

    def cagr_calculator(self):

        try:

            initial = float(
                input(
                    "Initial Value: "
                )
            )

            final = float(
                input(
                    "Final Value: "
                )
            )

            years = float(
                input(
                    "Years: "
                )
            )

            cagr = (
                (
                    final /
                    initial
                )
                **
                (
                    1 /
                    years
                )
                - 1
            ) * 100

            print(
                "\nCAGR:",
                round(
                    cagr,
                    2
                ),
                "%"
            )

        except:

            print(
                "Invalid Input"
            )

    def monthly_growth_estimator(self):

        try:

            amount = float(
                input(
                    "Monthly SIP: "
                )
            )

            rate = float(
                input(
                    "Annual Return %: "
                )
            )

            years = int(
                input(
                    "Years: "
                )
            )

            months = years * 12

            monthly_rate = \
                rate / 12 / 100

            future_value = 0

            for _ in range(
                    months):

                future_value = (
                    future_value
                    *
                    (
                        1 +
                        monthly_rate
                    )
                )

                future_value += amount

            print(
                "\nEstimated Value:"
            )

            print(
                round(
                    future_value,
                    2
                )
            )

        except:

            print(
                "Invalid Input"
            )

    def smart_insights(self):

        holdings = \
            self.get_holdings()

        total = len(
            holdings
        )

        print("\n")
        print("=" * 60)
        print(
            "SMART INSIGHTS"
        )
        print("=" * 60)

        if total < 3:

            print(
                "Increase Diversification"
            )

        if total >= 5:

            print(
                "Portfolio Well Diversified"
            )

        if total >= 10:

            print(
                "Excellent Diversification"
            )

        score = \
            self.investment_score()

        if score > 80:

            print(
                "Strong Portfolio"
            )

        elif score > 60:

            print(
                "Good Portfolio"
            )

        else:

            print(
                "Needs Improvement"
            )

    def health_report(self):

        print("\n")
        print("=" * 60)
        print(
            "PORTFOLIO HEALTH REPORT"
        )
        print("=" * 60)

        self.diversification_report()

        self.sector_allocation()

        self.risk_analysis()

        self.investment_score()

        self.smart_insights()


def analytics_menu(
        username
):

    analytics = \
        AdvancedAnalytics(
            "portfolios.json",
            username
        )

    while True:

        print("\n")
        print("=" * 50)
        print(
            "ADVANCED ANALYTICS"
        )
        print("=" * 50)

        print(
            "1. Diversification"
        )

        print(
            "2. Sector Allocation"
        )

        print(
            "3. Risk Analysis"
        )

        print(
            "4. Investment Score"
        )

        print(
            "5. CAGR Calculator"
        )

        print(
            "6. SIP Growth"
        )

        print(
            "7. Smart Insights"
        )

        print(
            "8. Health Report"
        )

        print(
            "9. Exit"
        )

        choice = input(
            "Choice: "
        )

        if choice == "1":

            analytics.diversification_report()

        elif choice == "2":

            analytics.sector_allocation()

        elif choice == "3":

            analytics.risk_analysis()

        elif choice == "4":

            analytics.investment_score()

        elif choice == "5":

            analytics.cagr_calculator()

        elif choice == "6":

            analytics.monthly_growth_estimator()

        elif choice == "7":

            analytics.smart_insights()

        elif choice == "8":

            analytics.health_report()

        elif choice == "9":

            break

        else:

            print(
                "Invalid Choice"
            )