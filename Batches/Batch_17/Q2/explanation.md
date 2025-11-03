Problem Statement:

https://leetcode.com/problems/right-triangles/description/


You are given a 2D boolean matrix grid.

A collection of 3 elements of grid is a right triangle if one of its elements is in the same row with another element and in the same column with the third element. The 3 elements may not be next to each other.

Return an integer that is the number of right triangles that can be made with 3 elements of grid such that all of them have a value of 1.

Sample Input:

grid = [
  [1, 0, 1],
  [1, 1, 0],
  [0, 1, 1]
]


Output:
6

Algorithm / Approach:

We use combinatorial counting instead of checking every triplet of 1s.

Precompute counts:

Count the number of 1s in each row → row_count[i]

Count the number of 1s in each column → col_count[j]

Iterate through each cell:
For every cell (i, j) that has a 1:

The number of possible right triangles with this cell as the right angle vertex
= (other 1s in the same row) × (other 1s in the same column)
→ (row_count[i] - 1) * (col_count[j] - 1)

Accumulate results:
Add all possible triangles for every 1 cell to get the total.

Why this works:
Each right triangle has a vertex (the right angle) where one leg lies horizontally and another vertically.
By counting how many other 1s exist in the same row and column, we directly compute how many triangles share that vertex.

Time Complexity:

Counting rows and columns: O(m × n)

Iterating all cells: O(m × n)
 Total: O(m × n)

Space Complexity:

Two extra arrays for row and column counts → O(m + n)

Example Input / Output:

Input:

grid = [
    [1, 1, 1],
    [1, 0, 1]
]


Output:

6


Explanation:
Each 1 in the grid that lies on both a row and column containing other 1s can form multiple right triangles by pairing horizontally and vertically.