def rob(nums, i=0):
    # Base case: if index i goes beyond the list length,
    # there are no more houses to rob, so return 0
    if i >= len(nums):
        return 0

    # Option 1: Rob the current house (nums[i])
    # and skip the next one (move to i + 2)
    rob_current = nums[i] + rob(nums, i + 2)

    # Option 2: Skip the current house
    # and move to the next one (i + 1)
    skip_current = rob(nums, i + 1)

    # Return the maximum of the two options
    return max(rob_current, skip_current)


# Example list of money in each house
nums = [2, 7, 9, 3, 1]

# Call the function starting from the first house (index 0)
result = rob(nums)

# Print the maximum amount the robber can steal
print("Maximum amount the robber can steal:", result)
