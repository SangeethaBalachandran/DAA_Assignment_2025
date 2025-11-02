def rob(nums):
    n = len(nums)

    # If there are no houses, nothing to rob
    if n == 0:
        return 0

    # If there is only one house, rob it
    if n == 1:
        return nums[0]

    # Create a DP array to store the maximum money up to each house
    dp = [0] * n

    # Base cases:
    # dp[0]: Max money from the first house
    dp[0] = nums[0]

    # dp[1]: Max money from first two houses
    # Either rob the first or the second one, whichever gives more
    dp[1] = max(nums[0], nums[1])

    # Fill the DP array from the third house onwards
    for i in range(2, n):
        # Option 1: Rob this house (add nums[i] to dp[i-2])
        # Option 2: Skip this house (dp[i-1])
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])

    # The last element of dp contains the maximum money that can be stolen
    return dp[-1]


# Example input
nums = [2, 7, 9, 3, 1]

# Function call
result = rob(nums)

# Output the result
print("Maximum amount the robber can steal:", result)
