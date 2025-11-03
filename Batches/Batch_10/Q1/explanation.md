
🧩 explanation.md
# 🧩 Q1 — Maximum Subarray Sum (Kadane’s Algorithm)

## 🔗 Problem Link
[LeetCode #53 — Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

---

## 💡 Algorithm / Approach Explanation

### Problem Overview  
You are given an integer array `nums`. The task is to find the **contiguous subarray** (containing at least one number) which has the **largest sum**, and return that sum.

Example:  
For `nums = [-2,1,-3,4,-1,2,1,-5,4]`,  
the subarray `[4, -1, 2, 1]` gives the largest sum = **6**.

---

### Naive Approach (O(n²))
- For every possible starting index, compute the sum for all possible subarrays.  
- Track the maximum sum seen so far.  
- **Disadvantage:** Too slow for large inputs (quadratic time complexity).

---

### Efficient Approach — Kadane’s Algorithm (Dynamic Programming)
Kadane’s algorithm efficiently finds the **maximum subarray sum** in **linear time**.

#### Steps:
1. Initialize two variables:
   - `curr_sum` = 0  
   - `max_sum` = first element of the array
2. Traverse each element `num` in `nums`:
   - If `curr_sum` becomes negative, reset it to 0.  
     (Because negative sum will reduce future subarray sums)
   - Add `num` to `curr_sum`
   - Update `max_sum = max(max_sum, curr_sum)`
3. Return `max_sum` after the loop ends.

---

### 🧠 Example Walkthrough

**Input:**  
`nums = [-2,1,-3,4,-1,2,1,-5,4]`

| Step | num | curr_sum | max_sum |
|------|-----|-----------|---------|
| 1 | -2 | 0 | -2 |
| 2 | 1 | 1 | 1 |
| 3 | -3 | 0 | 1 |
| 4 | 4 | 4 | 4 |
| 5 | -1 | 3 | 4 |
| 6 | 2 | 5 | 5 |
| 7 | 1 | 6 | 6 |
| 8 | -5 | 1 | 6 |
| 9 | 4 | 5 | 6 |

**Output:**  
`Maximum Subarray Sum = 6`  
**Explanation:** Subarray `[4, -1, 2, 1]` gives the maximum sum.

---

## ⏱️ Time and Space Complexity

| Type | Complexity | Explanation |
|------|-------------|--------------|
| **Time Complexity** | O(n) | Single traversal of array |
| **Space Complexity** | O(1) | Uses only constant variables |

---

## 🧩 Example Input / Output

**Input:**  
```python
nums = [-2,1,-3,4,-1,2,1,-5,4]


Output:

Maximum Subarray Sum = 6