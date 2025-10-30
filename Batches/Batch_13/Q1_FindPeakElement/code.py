# ========================================================
# BRUTE FORCE APPROACH
# ========================================================
# Paradigm: Exhaustive Search
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_peak_bruteforce(arr):
    n = len(arr)
    # Edge case: only one element
    if n == 1:
        return 0
    # Check if first element is a peak
    if arr[0] > arr[1]:
        return 0
    # Check middle elements
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return i
    # Check if last element is a peak
    if arr[-1] > arr[-2]:
        return n - 1
    # No peak found (theoretically not possible in valid input)
    return -1

# ========================================================
# OPTIMIZED APPROACH (BINARY SEARCH)
# ========================================================
# Paradigm: Divide and Conquer
# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_peak_binary_search(arr):
    n = len(arr)
    # If only one element
    if n == 1:
        return 0
    start = 1
    end = n - 2
    while start <= end:
        mid = start + (end - start) // 2
        # Check if mid is a peak
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
            return mid
        # If right neighbor is greater, move right
        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid - 1
    # Edge cases: first or last element
    if arr[0] > arr[1]:
        return 0
    if arr[-1] > arr[-2]:
        return n - 1
    return -1

# ========================================================
# MAIN PROGRAM (USER INPUT)
# ========================================================

print("=== FIND PEAK ELEMENT ===")
arr = list(map(int, input("Enter array elements: ").split()))
print("\n--- Brute Force Approach ---")
peak_index_bf = find_peak_bruteforce(arr)
if peak_index_bf != -1:
    print(f"Peak found at index {peak_index_bf} (Value = {arr[peak_index_bf]})")
else:
    print("No peak element found.")
print("\n--- Optimized Approach (Binary Search) ---")
peak_index_opt = find_peak_binary_search(arr)
if peak_index_opt != -1:
    print(f"Peak found at index {peak_index_opt} (Value = {arr[peak_index_opt]})")
else:
    print("No peak element found.")
