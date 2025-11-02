# Function to merge two sorted halves of an array
def merge(arr, start, mid, end):
    # Calculate lengths of left and right subarrays
    n1 = mid - start + 1
    n2 = end - mid

    # Create temporary arrays for left and right halves
    L = arr[start:start + n1]
    R = arr[mid + 1:mid + 1 + n2]

    # Initialize pointers for left (i), right (j), and merged array (k)
    i = j = 0
    k = start

    # Merge both halves in sorted order
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]   # Take element from left half
            i += 1
        else:
            arr[k] = R[j]   # Take element from right half
            j += 1
        k += 1

    # Copy any remaining elements of the left half
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy any remaining elements of the right half
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# Function to count reverse pairs using modified merge sort
def mergesort_and_count(arr, start, end):
    # Base case: if one or no element, no reverse pairs
    if start >= end:
        return 0
    
    # Find the middle index
    mid = (start + end) // 2

    # Recursively count reverse pairs in left and right halves
    count = mergesort_and_count(arr, start, mid) + mergesort_and_count(arr, mid + 1, end)

    # Count reverse pairs across the two halves
    # A reverse pair is (i, j) such that i < j and arr[i] > 2 * arr[j]
    j = mid + 1
    for i in range(start, mid + 1):
        while j <= end and arr[i] > 2 * arr[j]:
            j += 1
        count += (j - (mid + 1))

    # Merge the two sorted halves
    merge(arr, start, mid, end)

    # Return total reverse pair count
    return count


if __name__ == "__main__":
    # Input: space-separated integers
    nums = list(map(int, input("Enter numbers: ").split()))

    # Compute and print the number of reverse pairs
    result = mergesort_and_count(nums, 0, len(nums) - 1)
    print("Number of reverse pairs:", result)
