# 💹 Q2 — Best Time to Buy and Sell Stock IV

**Problem Link:** [LeetCode 188 — Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

---

## 🧠 Problem Description

You are given an integer `k` and an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.

Find the **maximum profit** you can achieve by completing at most `k` transactions.

A **transaction** consists of one buy and one sell of the stock.

You may **not hold more than one share of the stock at a time** — meaning, you must sell before you can buy again.

---

## 💡 Algorithm / Approach

This problem can be solved using **Dynamic Programming (DP)**.

### 🔹 Idea

We use a **3D DP array** `dp[ind][buy][cap]`:

- `ind`: current day index (0 to n)
- `buy`: 1 if we can buy on this day, 0 if we can sell
- `cap`: number of transactions remaining

`dp[ind][buy][cap]` stores the **maximum profit achievable** starting from day `ind`, given the current state (`buy` or `sell`) and remaining transaction capacity `cap`.

---

### 🔹 Transitions

1. **When `buy == 1` (we can buy):**
   - **Take:** Buy at this day → profit = `-prices[ind] + dp[ind+1][0][cap]`
   - **Not Take:** Skip this day → profit = `0 + dp[ind+1][1][cap]`
   - **Choose the maximum of both.**

2. **When `buy == 0` (we can sell):**
   - **Take:** Sell at this day → profit = `prices[ind] + dp[ind+1][1][cap-1]`
   - **Not Take:** Skip this day → profit = `0 + dp[ind+1][0][cap]`
   - **Choose the maximum of both.**

We compute this bottom-up from the last day backward.

---

## 🧩 Example

**Input:**
k = 2
prices = [3,2,6,5,0,3]


**Explanation:**
- You can complete at most 2 transactions.
- Best strategy:
  - Buy at price 2, sell at price 6 → Profit = 4  
  - Buy at price 0, sell at price 3 → Profit = 3  
- **Total Profit = 7**

**Output:**
7


---

## 🧮 Time and Space Complexity

| Complexity | Description |
|-------------|-------------|
| **Time Complexity** | O(n × 2 × k) → we iterate over all days, buy states, and transaction counts |
| **Space Complexity** | O(n × 2 × k) → 3D DP array to store results |

---

## 🧰 Code Implementation (Python)

```python
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
                        # Option 1: Buy stock at this day
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
