def solve(i, questions):
    # Base Case: If we reach beyond the last question, return 0
    if i >= len(questions):
        return 0

    # Option 1: Take the current question
    # Earn its points and skip next 'brainpower_i' questions
    take = questions[i][0] + solve(i + questions[i][1] + 1, questions)

    # Option 2: Skip the current question
    skip = solve(i + 1, questions)

    # Return the maximum points possible from either choice
    return max(take, skip)


# Example Input
questions = [[3, 2], [4, 3], [4, 4], [2, 5]]

# Starting recursion from the first question (index 0)
result = solve(0, questions)

# Print the results
print("Maximum points you can earn:", result)
