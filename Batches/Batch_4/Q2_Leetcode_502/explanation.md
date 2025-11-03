# LeetCode 502 — IPO  

## 🔗 Problem Link  
[LeetCode 502: IPO](https://leetcode.com/problems/ipo/)  

---

##  Problem Description  
You are given:  
- `k` → the maximum number of projects you can complete.  
- `w` → your initial capital.  
- Two arrays:  
  - `profits[i]`: profit from project `i`.  
  - `capital[i]`: minimum capital required to start project `i`.  

At any point, you can only start a project if your **current capital ≥ capital[i]**.  
Once you complete a project, your capital increases by its profit.  

**Objective:**  
Maximize your total capital after completing at most `k` projects.  

---

##  Intuition  
This problem simulates an investment strategy:  
- You have limited initial funds.  
- Each project requires a minimum investment and yields a profit.  
- As your capital grows, you unlock access to more projects.  

The key is to **prioritize projects with the highest profit among those you can currently afford**.  
This naturally suggests a **Greedy** strategy enhanced by efficient project selection.

---

##  Approach  

### 1️ Brute-Force Approach  
For each of the `k` selections:  
1. Iterate over all remaining projects.  
2. Among projects where `capital[i] ≤ current capital`, select the one with the **maximum profit**.  
3. Add its profit to your capital and mark it as completed.  

**Complexity:** `O(k * n)`  
This approach becomes inefficient for large inputs since it repeatedly scans all projects.

---

### 2️ Optimized Approach (Greedy + Max-Heap)  

To improve performance, combine **sorting** and a **max-heap**:

####  Steps
1. **Preprocessing:**  
   Pair each project as `(capital[i], profit[i])` and sort all projects by capital in ascending order.  

2. **Project Selection Loop (up to `k` times):**  
   - Add all projects whose capital ≤ current capital to a **max-heap**, keyed by profit.  
   - Select (pop) the project with the **highest profit** from the heap.  
   - Increase your capital by that profit.  
   - Repeat until you have done `k` projects or no feasible projects remain.  

####  Why it Works  
- Sorting ensures you process projects in increasing order of capital requirement.  
- The max-heap efficiently tracks the most profitable available projects at any point.  

---

## Example  

**Input:**
```
k = 2, w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
```

**Process:**

| Step | Current Capital | Affordable Projects | Max Profit Chosen | New Capital |
|------|------------------|----------------------|-------------------|--------------|
| 1 | 0 | [0] | +1 (Project 0) | 1 |
| 2 | 1 | [1, 2] | +3 (Project 2) | 4 |

 **Final Capital = 4**

---

##  Time and Space Complexity  

| Operation | Complexity |
|------------|-------------|
| Sorting Projects | `O(n log n)` |
| Heap Operations (up to k times) | `O(k log n)` |
| **Total Time Complexity** | **O(n log n + k log n)** |
| **Space Complexity** | **O(n)** |

---

##  Key Insight  
This is a **Greedy + Heap** problem:  
You iteratively choose the most profitable project you can afford, dynamically unlocking more options as your capital increases.  

It’s analogous to strategic investment — reinvesting profits to scale up your available opportunities.

---

##  Algorithm Summary  

```
1. Combine (capital, profit) for each project.
2. Sort by capital ascending.
3. Initialize a max-heap (profits).
4. For i in range(k):
     - Add all projects with capital ≤ current capital to heap.
     - If heap empty → break.
     - Pop max profit → add to capital.
5. Return final capital.
```

---
