def tsp(cost):
    n = len(cost)
    ALL = 1 << n                 # Total possible city subsets
    INF = float('inf')
    # dp[mask][i] = min cost to start at 0, visit cities in 'mask', and end at city i
    dp = [[INF] * n for _ in range(ALL)]
    dp[1][0] = 0                  # Starting at city 0 (mask = 000...001)
    for mask in range(ALL):
        for i in range(n):
            if not (mask & (1 << i)):   # Skip if city 'i' is not in mask
                continue
            for j in range(n):
                if mask & (1 << j) == 0:   # If city 'j' not visited yet
                    next_mask = mask | (1 << j)      # Add city 'j' to mask
                    dp[next_mask][j] = min(
                        dp[next_mask][j],
                        dp[mask][i] + cost[i][j]
                    )
    full_mask = (1 << n) - 1      # Mask with all cities visited
    ans = INF

    for i in range(n):
        ans = min(ans, dp[full_mask][i] + cost[i][0])  # Return to start city

    return ans
