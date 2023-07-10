# Creating a list of stock prices
price_of_stock = [7, 2, 4, 9, 3]

# Initializing a variable to keep track of weekly profit
weekly_profit = 0

# Storing the initial stock value as the first element of the price_of_stock list
initial_stock_value = price_of_stock[0]

# Looping through the price_of_stock list starting from the second element
for i in range(1, len(price_of_stock)-1):
    # Checking if the current stock price is greater than or equal to the initial stock value
    if price_of_stock[i] >= initial_stock_value:
        # Calculating the weekly profit as the difference between the current stock price and the initial stock value
        weekly_profit = price_of_stock[i] - initial_stock_value

# Printing the weekly profit
print("Total profit in this week:", weekly_profit)
