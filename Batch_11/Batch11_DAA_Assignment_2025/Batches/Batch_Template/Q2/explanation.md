🧠 Problem Link

https://leetcode.com/problems/jump-game-ii/

LeetCode #45 – Jump Game II

📝 Problem Statement

Given a 0-indexed array nums, where each element represents the maximum jump length from that position,
return the minimum number of jumps needed to reach the last index.

⚙️ Explanation
Brute Force Approach (Recursive):

From each index, recursively explore all possible jumps.

Add 1 for each jump made and take the minimum over all paths that reach the end.

Works for small arrays but is inefficient due to exponential growth.

Greedy Approach (Optimal BFS-like):

Treat the problem like a level-based traversal (similar to BFS).

Maintain:

farthest → farthest index reachable in the current level.

currentEnd → the end of the range for the current jump.

jumps → count of jumps made so far.

Traverse through the array:

Update farthest = max(farthest, i + nums[i]).

When i == currentEnd, it means you’ve reached the end of the current jump range:

Increment jumps.

Set currentEnd = farthest.

Continue until you reach the end of the array.

💡 Example

Input:
nums = [2, 3, 1, 1, 4]

Step-by-step (Greedy):

Step	i	Value	Farthest	Current End	Jumps
1	0	2	2	2	0
2	1	3	4	2	1
3	2	1	4	4	2

✅ Minimum Jumps = 2

🧮 Time and Space Complexity
Approach	Time Complexity	Space Complexity
Brute Force	O(2ⁿ)	O(n)
Greedy (Optimal)	O(n)	O(1)
🖥️ Output

Input: [2,3,1,1,4] → Output: 2
Input: [2,3,0,1,4] → Output: 2
