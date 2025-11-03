class Solution:
    def numberOfRightTriangles(self, grid: list[list[int]]) -> int:
        # Get number of rows (m) and columns (n)
        m, n = len(grid), len(grid[0])
        
        # Count how many 1s are present in each row and each column
        row_count = [sum(row) for row in grid]
        col_count = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        
        ans = 0  # Initialize the total number of right triangles
        
        # For every cell that contains a 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # If current cell is 1, possible triangles = 
                    # (other 1s in the same row) × (other 1s in the same column)
                    ans += (row_count[i] - 1) * (col_count[j] - 1)
        
        # Return total count of right triangles
        return ans
