# Q1: Maximum Subarray Sum (Kadane’s Algorithm)
# LeetCode #53

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = nums[0]
curr_sum = 0

for num in nums:
    if curr_sum < 0:
        curr_sum = 0
    curr_sum += num
    max_sum = max(max_sum, curr_sum)

print("Maximum Subarray Sum =", max_sum)
