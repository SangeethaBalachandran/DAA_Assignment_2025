class Solution(object):
    def maxProfit(self, k, prices):
        n = len(prices)
        
        # dp[ind][buy][cap] — max profit at index 'ind' with buy/sell state and 'cap' transactions left
        dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n + 1)]
        
        # Fill DP table from the last day backwards
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, k + 1):
                    
                    if buy:
                        # Option 1: Buy stock at this day+
                        take = -prices[ind] + dp[ind + 1][0][cap]
                        # Option 2: Skip buying
                        notTake = 0 + dp[ind + 1][1][cap]
                        profit = max(take, notTake)
                    else:
                        # Option 1: Sell stock at this day
                        take = prices[ind] + dp[ind + 1][1][cap - 1]
                        # Option 2: Skip selling
                        notTake = 0 + dp[ind + 1][0][cap]
                        profit = max(take, notTake)
                    
                    dp[ind][buy][cap] = profit
        
        # Start at day 0, with ability to buy, and 'k' transactions left
        return dp[0][1][k]
