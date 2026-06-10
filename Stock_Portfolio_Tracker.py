stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_investment = 0

print("Available Stocks:")
for stock in stock_prices:
    print(stock, ":", stock_prices[stock])

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Investment added:", investment)

    else:
        print("Stock not available.")

print("\nTotal Investment Value:", total_investment)

# Save result to file
file = open("portfolio.txt", "w")
file.write("Total Investment Value: " + str(total_investment))
file.close()

print("Portfolio saved to portfolio.txt")