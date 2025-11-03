from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        # Create a 2D array of lists to store results of subproblems
        dp = [[[] for _ in range(n)] for _ in range(n)]

        self._initialize_base_cases(expression, dp)

        # Fill the dp table for all possible subexpressions
        for length in range(3, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                self._process_subexpression(expression, dp, start, end)

        # Return the results for the entire expression
        return dp[0][n - 1]

    def _initialize_base_cases(self, expression: str, dp: List[List[List[int]]]):
        # Handle base cases: single digits and two-digit numbers
        for i, char in enumerate(expression):
            if char.isdigit():
                dig1 = ord(char) - ord("0")
                # Check for two-digit number (e.g., "10")
                if i + 1 < len(expression) and expression[i + 1].isdigit():
                    dig2 = ord(expression[i + 1]) - ord("0")
                    number = dig1 * 10 + dig2
                    dp[i][i + 1].append(number)
                # Single digit case
                dp[i][i].append(dig1)

    def _process_subexpression(
        self, expression: str, dp: List[List[List[int]]], start: int, end: int
    ):
        # Try all possible split positions
        for split in range(start, end + 1):
            if expression[split].isdigit():
                continue

            left_results = dp[start][split - 1]
            right_results = dp[split + 1][end]

            self._compute_results(expression[split], left_results, right_results, dp[start][end])

    def _compute_results(
        self,
        op: str,
        left_results: List[int],
        right_results: List[int],
        results: List[int],
    ):
        # Combine results using the operator
        for left_value in left_results:
            for right_value in right_results:
                if op == "+":
                    results.append(left_value + right_value)
                elif op == "-":
                    results.append(left_value - right_value)
                elif op == "*":
                    results.append(left_value * right_value)


# ------------------------------
# Example Usage (I/O Section)
# ------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    expression = "2-1-1"
    print(f"Expression: {expression}")
    print("Possible Results:", sol.diffWaysToCompute(expression))
    # Output: [0, 2]
    # Explanation:
    # (2-(1-1)) = 2
    # ((2-1)-1) = 0

    print()

    # Example 2
    expression = "2*3-4*5"
    print(f"Expression: {expression}")
    print("Possible Results:", sol.diffWaysToCompute(expression))
    # Output: [-34, -14, -10, -10, 10]
    # Explanation:
    # (2*(3-(4*5))) = -34
    # ((2*3)-(4*5)) = -14
    # ((2*(3-4))*5) = -10
    # (2*((3-4)*5)) = -10
    # (((2*3)-4)*5) = 10
