def maxProfit(prices):
    # Initialize total profit to 0
    profit = 0

    # Loop through the price list starting from the second day
    for i in range(1, len(prices)):
        # If today's price is higher than yesterday's price,
        # we can make a profit by buying yesterday and selling today
        if prices[i] > prices[i - 1]:
            # Add the profit from this transaction
            profit += prices[i] - prices[i - 1]

    # Return the total accumulated profit
    return profit
