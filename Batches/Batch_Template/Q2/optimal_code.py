def mostPoints(questions):
    n = len(questions)

    # DP array where dp[i] = max points that can be earned from question i to the end
    dp = [0] * (n + 1)

    # Traverse backwards from the last question
    for i in range(n - 1, -1, -1):
        # Unpack the current question details
        points, brainpower = questions[i]

        # Calculate the next index to jump after solving this question
        next_index = i + brainpower + 1

        # Option 1: Include the current question
        include = points
        if next_index < n:
            include += dp[next_index]  # Add future possible points

        # Option 2: Exclude the current question (skip to next)
        exclude = dp[i + 1]

        # Choose the better option
        dp[i] = max(include, exclude)

    # The result is stored at the first position
    return dp[0]


# Example Input
questions = [[3, 2], [4, 3], [4, 4], [2, 5]]

# Output
result = mostPoints(questions)
print("Maximum points you can earn:", result)
