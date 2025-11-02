
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Sets to track attacked columns and diagonals
        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        res = []  # Stores all valid board configurations
        board = [["."] * n for _ in range(n)]  # Initialize empty board

        # Recursive backtracking function
        def backtrack(r):
            # Base condition: All rows processed → valid configuration
            if r == n:
                # Convert board to list of strings
                res.append(["".join(row) for row in board])
                return

            # Try placing queen in each column of current row
            for c in range(n):
                # Skip if column or diagonal under attack
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Place queen
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Recurse to next row
                backtrack(r + 1)

                # Backtrack (remove queen)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        # Start recursion from row 0
        backtrack(0)
        return res


# ============================================
# Main (Driver) Code
# ============================================
if _name_ == "_main_":
    # Take input from the user
    n = int(input("Enter the value of N (size of chessboard): "))

    # Create an object of Solution class
    solver = Solution()

    # Get all possible solutions
    solutions = solver.solveNQueens(n)

    # Display results
    print(f"\nTotal Solutions for {n}-Queens: {len(solutions)}\n")

    # Print each valid board configuration
    for i, board in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for row in board:
            print(row)
        print()
