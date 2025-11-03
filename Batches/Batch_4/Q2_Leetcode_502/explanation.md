**Problem Link: https://leetcode.com/problems/ipo/**

**Naive (Greedy) Approach:**
In this method, for each of the k selections, we go through all projects and choose the most profitable one that can be started with the current capital w. After completing that project, we add its profit to w and mark it as done.

**Algorithm Steps:**
1. Repeat k times:
   - Find the project with the highest profit among those whose required capital ≤ current capital.
   - Add that profit to current capital.
   - Mark that project as completed.
2. Stop early if no project can be started.

Time Complexity: O(k * n)
Space Complexity: O(1)

**Optimized (Heap-based) Approach:**
This method improves performance using sorting and a max heap (priority queue).

**Algorithm Steps:**
1. Sort all projects by capital.
2. Use a max heap to store profits of projects that can be afforded with current w.
3. For each of the k selections:
   - Add all affordable projects’ profits into the heap.
   - Pop the highest profit from the heap and add it to w.
   - Continue until k selections or no projects are available.

Time Complexity: O(n log n)
Space Complexity: O(n)

**Example Input/Output:**
Input:
k = 2, w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]

**Output:**
4

**Explanation:**
Start project 1 (profit = 1) → total = 1
Then start project 3 (profit = 3) → total = 4
