
# Hardcoded stock prices (per share, in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 175,
    "MSFT": 420,
}


def get_portfolio():
    """Ask the user which stocks they own and how many shares."""
    portfolio = {}

    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))
    print("Type 'done' when you're finished adding stocks.\n")

    while True:
        stock = input("Enter stock symbol: ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found in our list. Try again.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity < 0:
                print("Quantity can't be negative.\n")
                continue
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"Added {quantity} shares of {stock}.\n")

    return portfolio


def calculate_total(portfolio):
    """Calculate total investment value."""
    total = 0
    breakdown = []

    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * quantity
        total += value
        breakdown.append((stock, quantity, price, value))

    return total, breakdown


def save_report(breakdown, total, filename="portfolio_report.txt"):
    """Save the investment report to a text file."""
    with open(filename, "w") as f:
        f.write("Stock Portfolio Report\n")
        f.write("=" * 40 + "\n")
        for stock, quantity, price, value in breakdown:
            f.write(f"{stock}: {quantity} shares x ${price} = ${value}\n")
        f.write("=" * 40 + "\n")
        f.write(f"Total Investment: ${total}\n")
    print(f"\nReport saved to {filename}")


def main():
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks added. Exiting.")
        return

    total, breakdown = calculate_total(portfolio)

    print("\n--- Investment Summary ---")
    for stock, quantity, price, value in breakdown:
        print(f"{stock}: {quantity} shares x ${price} = ${value}")
    print(f"Total Investment: ${total}")

    save = input("\nSave this report to a file? (y/n): ").lower().strip()
    if save == "y":
        save_report(breakdown, total)


if __name__ == "__main__":
    main()