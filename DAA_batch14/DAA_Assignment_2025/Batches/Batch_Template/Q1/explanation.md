Best Time to Buy and Sell Stock II (LeetCode #122)
Problem Description
You are given an integer array prices where prices[i] represents the price of a given stock on the i-th day.
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
However, you must sell the stock before you buy again.
Your goal is to maximize your total profit.

Example:

Input:
prices = [7, 1, 5, 3, 6, 4]

Output:
7

Explanation:
Buy at 1 → Sell at 5 → Profit = 4
Buy at 3 → Sell at 6 → Profit = 3
Total Profit = 4 + 3 = 7

Approach (Greedy):
The problem can be solved using a greedy algorithm.
Instead of trying to find local minima and maxima, we simply add up every increase in price.
Whenever today’s price is higher than yesterday’s, we can profit by buying yesterday and selling today.
This effectively captures all upward movements in the stock price.


Time Complexity: O(n)
Space Complexity: O(1)