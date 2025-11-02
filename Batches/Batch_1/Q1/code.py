def merge_sort(counts_arr, counts):
    # Base condition: If array length is more than 1, divide and merge
    if len(counts_arr) > 1:
        mid = len(counts_arr) // 2
        left = counts_arr[:mid]   # Left half
        right = counts_arr[mid:]  # Right half

        # Recursively sort both halves
        merge_sort(left, counts)
        merge_sort(right, counts)

        i = j = 0  # Pointers for left and right halves
        merged = []  # Temporary array to store merged elements

        # Merge step
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                # All elements before j in right[] are smaller than left[i]
                counts[left[i][1]] += j
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Add remaining elements from left[] and update counts
        while i < len(left):
            counts[left[i][1]] += j
            merged.append(left[i])
            i += 1

        # Add remaining elements from right[]
        while j < len(right):
            merged.append(right[j])
            j += 1

        # Copy merged elements back to original array
        for k in range(len(counts_arr)):
            counts_arr[k] = merged[k]


def countSmaller(nums):
    n = len(nums)
    counts = [0] * n  # To store result counts
    counts_arr = []

    # Store each number with its original index
    for i in range(n):
        counts_arr.append((nums[i], i))

    # Perform modified merge sort
    merge_sort(counts_arr, counts)
    return counts

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = countSmaller(arr)
    print(*result)
