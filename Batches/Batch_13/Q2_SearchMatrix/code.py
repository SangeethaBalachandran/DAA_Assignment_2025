"""
----------------------------------------------------------
Q2: Search a 2D Matrix II  (LeetCode #240)
----------------------------------------------------------
Problem Statement:
Write an efficient algorithm that searches for a target value in an m x n 
integer matrix. This matrix has the following properties:
    • Integers in each row are sorted in ascending order (left → right).
    • Integers in each column are sorted in ascending order (top → bottom).
----------------------------------------------------------
Constraints:
1 <= m, n <= 300
-10^9 <= matrix[i][j], target <= 10^9
----------------------------------------------------------
"""

# ---------------------------------------------------------------
# Approach 1 : Brute Force (Naive, Exhaustive Search)
# ---------------------------------------------------------------
# Check every element one by one.
# Time : O(m * n)
# Space : O(1)
# ---------------------------------------------------------------

def search_matrix_bruteforce(matrix, target):
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False

# ---------------------------------------------------------------
# Approach 2 : Binary Search on Each Row
# ---------------------------------------------------------------
# Since every row is sorted, we can apply binary search
# separately on each row.
# Time : O(m * log n)
# Space : O(1)
# ---------------------------------------------------------------

def search_matrix_row_binary(matrix, target):
    for row in matrix:
        low = 0
        high = len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    return False

# ---------------------------------------------------------------
# Approach 3 : Staircase Search (Greedy)
# ---------------------------------------------------------------
# Start from top-right corner and move left or down based on value.
# Time : O(m + n)
# Space : O(1)
# ---------------------------------------------------------------

def search_matrix_staircase(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1   # start at top-right

    while row < m and col >= 0:
        current = matrix[row][col]

        if current == target:
            return True
        elif current > target:
            col -= 1     # move left
        else:
            row += 1     # move down

    return False

# ---------------------------------------------------------------
# User Input Section
# ---------------------------------------------------------------

m, n = map(int, input("Enter matrix size (rows cols): ").split())
matrix = []
print("Enter the matrix elements row-wise:")
for _ in range(m):
    matrix.append(list(map(int, input().split())))

target = int(input("Enter target value: "))

# ---------------------------------------------------------------
# Uncomment whichever approach you want to test
# ---------------------------------------------------------------

# print("Result (Brute Force):", search_matrix_bruteforce(matrix, target))
# print("Result (Binary Search):", search_matrix_row_binary(matrix, target))
found = search_matrix_staircase(matrix, target)
print("Target found?", "Yes" if found else "No")


