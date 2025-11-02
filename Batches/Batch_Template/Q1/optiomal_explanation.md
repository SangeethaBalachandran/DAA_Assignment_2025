# 🏠 House Robber — LeetCode Problem

## Problem Link  
[LeetCode — House Robber](https://leetcode.com/problems/house-robber/)

---

## Problem Description  
You are a professional robber planning to rob houses along a street.  
Each house has a certain amount of money.  
However, **adjacent houses have security systems connected**, and if two adjacent houses are robbed, the police will be alerted.  

Your task is to find the **maximum amount of money** you can rob tonight **without alerting the police**.

---

## ⚙️ Algorithm / Approach Explanation  

### Idea:
We use Dynamic Programming (DP) to decide for each house whether to rob it or skip it.

At each house:
- Rob this house → add its money and skip the previous one (nums[i] + dp[i-2])
- Skip this house → take the previous maximum (dp[i-1])
We take the maximum of both.

### Recursive Relation:
dp[i] = max(nums[i] + dp[i-2], dp[i-1])

### Base Cases:
- dp[0] = nums[0]
- dp[1] = max(nums[0], nums[1])

From the 3rd house onwards:
dp[i] = max(nums[i] + dp[i-2], dp[i-1])

---

## Example  

### Input:
nums = [2, 7, 9, 3, 1]

### Output:
Maximum amount the robber can steal: 12

### Explanation:
Step-by-step Process:
- House 0: 2 → only one house, so rob it → dp[0] = 2  
- House 1: 7 → max(2, 7) = 7 → dp[1] = 7  
- House 2: 9 → max(9 + 2, 7) = 11 → dp[2] = 11  
- House 3: 3 → max(3 + 7, 11) = 11 → dp[3] = 11  
- House 4: 1 → max(1 + 11, 11) = 12 → dp[4] = 12  

Maximum = 12