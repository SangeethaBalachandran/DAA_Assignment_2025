# House Robber — LeetCode Problem

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
At each house, you have two choices:
1. **Rob the current house** → skip the next house (move to `i + 2`)
2. **Skip the current house** → move to the next one (`i + 1`)

We pick the option that gives the **maximum total amount**.

### Recursive Relation:

rob(i) = max(nums[i] + rob(i + 2), rob(i + 1))

### Base Case:
If index `i` goes beyond the list length → return `0`  
(because there are no more houses left to rob).

---

## Example  

### Input:
```python
nums = [2, 7, 9, 3, 1]
```

### Output:
Maximum amount the robber can steal: 12

---

### Explanation :

Step-by-step Process:
- Rob house 0 → 2 + rob(2)
- Skip house 0 → rob(1)

Recursion explores all possibilities and finds:
- Rob houses [2, 9, 1] → Total = 12
- Rob houses [7, 3] → Total = 10

**Maximum amount = 12**
