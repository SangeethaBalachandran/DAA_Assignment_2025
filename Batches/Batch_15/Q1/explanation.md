# Task Scheduler Problem Explanation

## 🔗 Problem Link
[LeetCode #621 - Task Scheduler](https://leetcode.com/problems/task-scheduler/)

---

##  Problem Description
You are given a list of tasks represented by capital letters (like `["A","A","A","B","B","C"]`) and a non-negative integer `n` which represents the *cooling interval* between two same tasks.
Each task takes exactly one time unit to complete.

You must find the **least number of time units** required to finish all the given tasks.

---

##  Algorithm / Approach Explanation

### Idea
We want to schedule tasks such that the same type of task has at least `n` time units between consecutive executions.

To minimize idle time, the scheduling pattern is primarily determined by the most frequent tasks.

### Steps

1. **Count task frequencies**
   Use a dictionary to count occurrences of each task.

2. **Find the maximum frequency (`max_freq`)**
   This represents how many times the most frequent task appears.

3. **Find how many tasks have this maximum frequency (`count_max`)**
   If multiple tasks have the same highest frequency, count all of them.

4. **Compute the minimum time needed (formula):**
   ```
   total_time = (max_freq - 1) * (n + 1) + count_max
   ```
   - `(max_freq - 1)` → number of full cycles excluding the last one
   - `(n + 1)` → one slot for the frequent task + n cooldowns
   - `count_max` → tasks that appear the maximum number of times

5. **Return the maximum between total tasks and computed time**
   ```python
   return max(len(tasks), total_time)
   ```
   If there are enough tasks to fill idle slots, the total time will just be the total number of tasks.

---

## ⏱️ Time and Space Complexity

| Complexity | Description |
|-------------|--------------|
| **Time:**  | O(T), where T is the number of tasks (for counting frequencies) |
| **Space:** | O(1), since there are only 26 possible uppercase task types |

---

##  Example Input / Output

### Example 1
**Input:**
```python
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(leastInterval(tasks, n))
```
**Output:**
```
8
```
**Explanation:**
Possible schedule:
```
A → B → idle → A → B → idle → A → B
```
Total time = 8 units.

---

### Example 2
**Input:**
```python
tasks = ["A", "A", "A", "B", "B", "B"]
n = 0
print(leastInterval(tasks, n))
```
**Output:**
```
6
```
**Explanation:**
No cooldown needed; just execute all tasks one after another.

---

## Summary
| Step | Purpose |
|------|----------|
| Count frequencies | Identify most frequent tasks |
| Find `max_freq` and `count_max` | Determine schedule pattern |
| Apply formula | Derive minimal possible time |
| Return final result | Ensure all tasks fit schedule |
