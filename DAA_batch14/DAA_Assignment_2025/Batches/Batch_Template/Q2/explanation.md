Candy Distribution (LeetCode #135)
Problem Statement:
There are n children standing in a line, each child has a rating value given by the integer array ratings.
You must give candies to these children following two rules:
Each child must have at least one candy.
Children with a higher rating get more candies than their immediate neighbors.
Return the minimum number of candies you must give to satisfy the conditions.

Example:
Input:
ratings = [1, 0, 2]

Output:
5

Explanation:
Child 1 (rating 1) → gets 2 candies
Child 2 (rating 0) → gets 1 candy
Child 3 (rating 2) → gets 2 candies
Total = 5 candies

Approach (Slope Method):
This approach views the ratings array as a series of uphill and downhill slopes:
When ratings increase, distribute increasing candies (1, 2, 3, ...).
When ratings decrease, distribute decreasing candies (3, 2, 1, ...).
Handle equal ratings by resetting slope counting.
Subtract the smaller slope length to avoid double counting the peak.
This ensures all conditions are met with minimum candies.

Step-by-step Explanation:
Start with each child having 1 candy → candies = n
Traverse through the ratings list:
Skip equal ratings (flat region).
Count increasing slope length (peak).
Count decreasing slope length (valley).
For each slope:
Add candies equal to slope length.
Remove overlap (min(peak, valley)) since the top child (peak) counted twice.
Return total candies.

Time Complexity	O(n) — Single pass through ratings
Space Complexity O(1) — Constant extra space
