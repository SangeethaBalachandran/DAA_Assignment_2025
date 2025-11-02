# LeetCode Problem — Solving Questions With Brainpower

**Problem Link:** [LeetCode - Solving Questions With Brainpower](https://leetcode.com/problems/solving-questions-with-brainpower/)

---

## Problem Description

You are given a 2D array `questions`, where `questions[i] = [points_i, brainpower_i]`.

- If you solve question `i`, you earn `points_i` points.
- After solving it, you must skip the next `brainpower_i` questions before you can solve another.

Your goal is to **maximize the total points** you can earn.

---

## Algorithm / Approach

We use **Dynamic Programming (DP)** to solve this efficiently by avoiding repeated recalculations.  
For each question, we have **two choices**:

1. **Take** the current question:
   - Earn its points (`points_i`).
   - Skip the next `brainpower_i` questions.
   - Add the result from the next available question: `dp[i + brainpower_i + 1]`.

2. **Skip** the current question:
   - Simply move to the next question: `dp[i + 1]`.

We compute this from **right to left** (bottom-up), so that future results are already known.

**Formula:**

dp[i] = max(points[i] + dp[i + brainpower[i] + 1], dp[i + 1])

---

## Example Input and Output

### **Example 1**

**Input:**
```python
questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
```

**Output:**
Maximum points you can earn: 5

**Explanation:**
- Solve question 0 → earn 3 points, skip next 2 → move to question 3.
- Solve question 3 → earn 2 points.
- **Total = 3 + 2 = 5**
