// Sample code file for Batch Template Q1
def canPartition(nums):
    # Calculate the total sum of all elements in the array
    total_sum = sum(nums)

    # If the total sum is odd, we cannot split it into two equal subsets
    if total_sum % 2 != 0:
        return False

    # The target sum for each subset should be half of the total sum
    target = total_sum // 2

    # Create a DP array where dp[j] means whether a subset with sum 'j' is possible
    dp = [False] * (target + 1)

    # Base case: sum 0 is always possible (empty subset)
    dp[0] = True

    # Iterate through each number in the array
    for num in nums:
        # Traverse backwards to ensure each number is used only once
        for j in range(target, num - 1, -1):
            # If we can make sum 'j - num', then we can also make sum 'j'
            dp[j] = dp[j] or dp[j - num]
    
    # Final answer: whether it's possible to form a subset with sum equal to 'target'
    return dp[target]
