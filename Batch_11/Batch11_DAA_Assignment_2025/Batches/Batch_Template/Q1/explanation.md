Problem Statement

https://leetcode.com/problems/jump-game/

You are given an integer array nums, where each element represents your maximum jump length from that position.
Return true if you can reach the last index, otherwise false.

⚙️ Explanation
Brute Force Approach (Recursive Backtracking):

Start from the first index.

From each position, try all possible jumps (from 1 to nums[i]).

Recursively check if you can reach the last index.

If any path can reach the last index → return true.

Otherwise, return false.

This method explores all possible paths and works correctly for small inputs, but is very slow for larger arrays due to repeated computations.

Greedy Approach (Optimal):

Keep track of the maximum reachable index (reachable) at each step.

Traverse the array from left to right.

If at any point, i > reachable, it means you are stuck and cannot move forward → return false.

Otherwise, update reachable = max(reachable, i + nums[i]).

If reachable is greater than or equal to the last index → return true.

💡 Example

Input:
nums = [2, 3, 1, 1, 4]

Step-by-step (Greedy):

Index	Value	Reachable	Action
0	2	2	reachable = max(0, 0+2) = 2
1	3	4	reachable = max(2, 1+3) = 4
2	1	4	reachable still 4

✅ Since reachable (4) ≥ last index (4), we can reach the end.

🧮 Time and Space Complexity
Approach	Time Complexity	Space Complexity
Brute Force	O(2ⁿ)	O(n)
Greedy (Optimal)	O(n)	O(1)
🖥️ Output

Input: [2,3,1,1,4] → Output: true
Input: [3,2,1,0,4] → Output: false