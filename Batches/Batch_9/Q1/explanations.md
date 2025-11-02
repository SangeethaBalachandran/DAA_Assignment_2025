Problem Link:

  https://leetcode.com/problems/n-queens/

Algorithm / Approach (Backtracking with Column & Diagonal Tracking):

  Place one queen per row using recursive backtracking.

  Maintain three sets to track attacked positions:

  col → columns already occupied.

  posDiag → positive diagonals (r + c).

  negDiag → negative diagonals (r - c).

  For each row r, iterate over all columns c:

  Skip placement if (c ∈ col) or (r + c ∈ posDiag) or (r - c ∈ negDiag).

  Otherwise, place a queen, mark attacked lines, and move to the next row.

  After exploring, remove the queen (backtrack).

  When r == n, all queens are safely placed → store configuration.

  This ensures no two queens share the same row, column, or diagonal.

Time and Space Complexity:

    Complexity Type	 Value
    Time Complexity	  O(N!)
    Space Complexity	O(N²)
    
Example Input/Output:

  Input:

    N = 4


  Output:

    [
     [".Q..",
      "...Q",
      "Q...",
      "..Q."],
    
     ["..Q.",
      "Q...",
      "...Q",
      ".Q.."]
    ]


Total Solutions = 2
