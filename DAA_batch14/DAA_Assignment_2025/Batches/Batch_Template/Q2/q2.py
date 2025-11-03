def candy(ratings):
    n = len(ratings)
    candies = n  # Every child gets at least 1 candy
    i = 1

    while i < n:
        # Skip equal ratings (no slope)
        if ratings[i] == ratings[i - 1]:
            i += 1
            continue

        # Count increasing slope (left to right)
        peak = 0
        while i < n and ratings[i] > ratings[i - 1]:
            peak += 1
            candies += peak  # Add extra candies for increasing sequence
            i += 1

        # Count decreasing slope (right to left)
        valley = 0
        while i < n and ratings[i] < ratings[i - 1]:
            valley += 1
            candies += valley  # Add extra candies for decreasing sequence
            i += 1

        # Adjust overlapping candy at the peak (counted twice)
        candies -= min(peak, valley)

    return candies
