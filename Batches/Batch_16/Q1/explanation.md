
# 🧩 Q1 — Partition Equal Subset Sum

**Problem Link:** [LeetCode 416 — Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

---

## 🧠 Problem Description

Given a non-empty array `nums` containing only positive integers, determine if the array can be partitioned into **two subsets** such that the **sum of elements in both subsets is equal**.

---

## 💡 Algorithm / Approach

This problem is a variation of the **Subset Sum Problem** and can be solved using **Dynamic Programming**.

### 🔹 Key Idea

- The goal is to check whether there exists a subset of numbers whose sum equals **half of the total array sum**.
- If the total sum is **odd**, we can immediately return `False` because we cannot divide an odd number into two equal integers.
- If the total sum is **even**, we set the target as `total_sum / 2`.
- We use a **1D DP array** where `dp[j]` indicates whether a subset sum of `j` is possible.
- Initially, `dp[0] = True` because a subset with sum 0 is always possible (empty subset).
- For each number `num` in `nums`, we iterate `j` from `target` down to `num` and update:

- Finally, `dp[target]` tells us whether the target sum is achievable.

---

## 🧩 Example

**Input:**  [1,5,11,5]

**Explanation:**
- Total sum = 22 → target = 11  
- Using dynamic programming, we find that a subset `{11}` or `{5,5,1}` gives sum 11.

**Output:**
 True
---

## 🧮 Time and Space Complexity

| Complexity | Description |
|-------------|--------------|
| **Time Complexity** | O(n * target) → where `n` is the number of elements and `target = total_sum / 2` |
| **Space Complexity** | O(target) → uses a 1D DP array of size `target + 1` |

---

## 🧰 Code Implementation (Python)

```python
def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True  # sum 0 is always possible

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]
