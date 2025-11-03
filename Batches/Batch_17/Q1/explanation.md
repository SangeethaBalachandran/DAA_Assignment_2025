Problem link: 
[LeetCode - 241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)



 Algorithm / Approach Explanation

The problem asks us to compute all possible results from an arithmetic expression by adding parentheses in all valid ways.  
We can solve this using **Dynamic Programming (DP)** or **Divide and Conquer with Memoization**.

 Approach (DP version used here):
1. We create a 2D list `dp[i][j]`, where each cell stores all possible results for the subexpression from index `i` to `j`.
2. Base cases:  
   - If the substring is a number (single or two-digit), store it directly in `dp[i][i]` or `dp[i][i+1]`.
3. For longer expressions:  
   - For each operator position (like `+`, `-`, `*`), split the expression into left and right parts.  
   - Combine all results from `dp[start][split-1]` and `dp[split+1][end]` using the operator.
4. Finally, `dp[0][n-1]` holds all possible results for the entire expression.



 Time and Space Complexity

- **Time Complexity:** O(N³)  
  (We check all possible splits and combine results for each subexpression.)
- **Space Complexity:** O(N²)  
  (We store results for all possible subexpressions in the DP table.)

---

 Example Input/Output

#### Example 1
**Input:**  
```
expression = "2-1-1"
```
**Output:**  
```
[0, 2]
```
**Explanation:**  
```
(2-(1-1)) = 2  
((2-1)-1) = 0
```

---

#### Example 2
**Input:**  
```
expression = "2*3-4*5"
```
**Output:**  
```
[-34, -14, -10, -10, 10]
```
**Explanation:**  
```
(2*(3-(4*5))) = -34  
((2*3)-(4*5)) = -14  
((2*(3-4))*5) = -10  
(2*((3-4)*5)) = -10  
(((2*3)-4)*5) = 10
```
