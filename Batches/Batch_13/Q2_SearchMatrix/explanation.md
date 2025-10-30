## **Q2 – Search a 2D Matrix II**

### **Problem Link:**

LeetCode 240 – Search a 2D Matrix II  
**https://leetcode.com/problems/search-a-2d-matrix-ii**

## **Problem Statement:**

Given an m x n matrix where:

1. Each row is sorted in ascending order from left to right.  
2. Each column is sorted in ascending order from top to bottom.

We need to determine whether a specific target value is present in the matrix.

### **1\. Brute Force Approach**

**Paradigm:** Exhaustive Search  
**Concept:**  
 The brute force solution checks every single element of the matrix until it finds the target value or concludes it is not present.This approach does not take advantage of the matrix’s sorted property; it simply scans all elements sequentially.

**Step-by-Step Working:**

1. Start from the first row and first column.

2. Compare each element with the target.

3. If any element equals the target, return success.

4. If all elements are traversed without finding the target, return failure.

**Example:**  
 For the above matrix, if we search for 5, the algorithm will check elements as follows:  
 1 → 4 → 7 → 11 → 15 → 2 → 5 → found.  
 Hence, the target is located after seven comparisons.

**Complexity Analysis:**

* Time Complexity: **O(m × n)** since every element is checked once.

* Space Complexity: **O(1)** as no extra memory is used.

### **2\. Binary Search on Each Row**

**Paradigm:** Divide and Conquer

**Concept**:  
 Since each row is sorted, we can apply binary search on every row instead of scanning it linearly.Binary search divides each row repeatedly into halves, checking whether the target lies in the left or right portion, thereby reducing the number of comparisons drastically.

**Step-by-Step Working:**

1. For each row, initialize two pointers: one at the start and one at the end.

2. Find the middle element of the row.

3. If the middle element equals the target, the search ends successfully.

4. If the middle element is greater than the target, the search continues in the left half.

5. If the middle element is smaller, search the right half.

6. Repeat this process for every row until the target is found or all rows are checked.

**Example:**  
 In the above matrix, for target 5:

* Row 1 → middle element \= 7 → 5 \< 7 → search left half → found at position (1,2).

**Complexity Analysis:**

* Time Complexity: **O(m × log n)**,since binary search takes log n time for each row.

* Space Complexity: **O(1)**.

### **3\. Staircase Search (Optimal Approach)**

**Paradigm:** Greedy / Reduction-based Search

**Concept:**  
            This method uses a clever greedy approach based on the sorted structure of both rows and columns.It starts from the top-right corner of the matrix and decides whether to move left or down based on comparisons.This effectively reduces the search space in every step.

**Reason for Choosing Top-Right Corner:**

* The top-right element is the largest in its row and smallest in its column.

* Hence, from this position, we can make a clear decision:

  * If the target is smaller, move left (since elements to the left are smaller).

  * If the target is larger, move down (since elements below are larger).

**Step-by-Step Working:**

1. Start from the top-right corner of the matrix.

2. Compare the current element with the target.

3. If they match, the search ends successfully.

4. If the current element is larger than the target, move one column left.

5. If it is smaller than the target, move one row down.

6. Continue until the indices go out of bounds or the element is found.

**Complexity Analysis:**

* Time Complexity: **O(m \+ n)**

* Space Complexity: **O(1)**

**Why It’s Optimal:**  
 At each step, either one row or one column is eliminated from the search space.  
 Hence, the total number of steps is at most m \+ n.

Example Dry Run:  
 Target \= 5

| Step | Row | Column | Element | Action |
| ----- | ----- | ----- | ----- | ----- |
| 1 | 0 | 4 | 15 | 15 \> 5 → Move Left |
| 2 | 0 | 3 | 11 | 11 \> 5 → Move Left |
| 3 | 0 | 2 | 7 | 7 \> 5 → Move Left |
| 4 | 0 | 1 | 4 | 4 \< 5 → Move Down |
| 5 | 1 | 1 | 5 | 5 \== target → Found |

Thus, the target is found after only five comparisons, compared to twenty-five in the brute force approach.

## Comparative Analysis

| Approach | Paradigm | Time Complexity | Space Complexity | Efficiency |
| ----- | ----- | ----- | ----- | ----- |
| Brute Force | Exhaustive Search | O(m × n) | O(1) | Low |
| Binary Search | Divide & Conquer | O(m × log n) | O(1) | Moderate |
| Staircase Search | Greedy / Reduction | O(m \+ n) | O(1) | High (Optimal) |

## **Sample Input/Output**

**Input:**

Enter matrix size (rows cols): 5 5                  Enter target value: 5  
Enter the matrix row-wise:                              Output:  
1 4 7 11 15                                                                  Target found? Yes  
2 5 8 12 19                                                         Enter target value: 20  
3 6 9 16 22                                                         Output:  
10 13 14 17 24                                                             Target found? No  
18 21 23 26 30

**Result:**

The experiment was successfully conducted to search for a target element in a sorted 2D matrix using three different paradigms — Exhaustive Search, Divide and Conquer, and Greedy Reduction.  
 Among these, the Staircase Search approach proved to be the most optimal with a time complexity of O(m \+ n).

## **Conclusion:**

This experiment highlights how the efficiency of an algorithm improves when problem properties are effectively utilized.While the brute force method provides a basic understanding of the problem, more advanced paradigms like Divide and Conquer and Greedy significantly optimize the process.By starting at a strategic position (top-right corner), the Staircase Search leverages both the row and column order, reducing redundant comparisons and achieving the best possible time complexity for this problem.Hence, the problem demonstrates the role of algorithmic design paradigms in enhancing computational performance.

