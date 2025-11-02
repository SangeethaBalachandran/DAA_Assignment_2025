Problem Link: 
  https://www.geeksforgeeks.org/problems/travelling-salesman-problem2732/1

Algorithm / Approach (Bitmask Dynamic Programming):

  Represent the visited cities using a bitmask, where the i-th bit is 1 if city i has been visited.
  Maintain a DP table dp[mask][pos] which stores the minimum travel cost to:
  Start from the current city pos
  Visit all cities represented in mask
  And eventually return to the starting city.
  Start with mask = 1 (only city 0 visited) and pos = 0 (starting city).
  At each step, try moving to any unvisited city city and update the result:

    dp[mask][pos] = min(
    dp[mask][pos],
    cost[pos][city] + dp[mask | (1 << city)][city]
    )
  Continue this recursion until all cities have been visited:

    if mask == VISITED_ALL:
        return cost[pos][0]   // return back to the start

  The final answer is obtained from:
  
        dp[1][0]

Time and Space Complexity:

    | Complexity Type  | Value      |
    | ---------------- | ---------- |
    | Time Complexity  | O(n² × 2ⁿ) |
    | Space Complexity | O(n × 2ⁿ)  |

Example input/output:

Input:
  
  N = 4
  cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
  ]
Output:
  80         #cost[0][1] + cost[1][3] + cost[3][2] + cost[2][0]= 10 + 25 + 30 + 15

