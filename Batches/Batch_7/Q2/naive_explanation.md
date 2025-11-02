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

We use **recursion with decision making** — for each question, we have **two choices**:

1. **Take** the current question:
   - Add its points.
   - Skip the next `brainpower_i` questions.

2. **Skip** the current question:
   - Move to the next question.

At each step, we return the maximum of these two choices.

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