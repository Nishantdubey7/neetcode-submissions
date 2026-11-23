class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        cuts = [0] + sorted(cuts) + [n]
        dp = [[0] * (m + 2) for _ in range(m + 2)]

        for length in range(2, m + 2):
            for i in range(m + 2 - length):
                j = i + length
                dp[i][j] = float("inf")
                for mid in range(i + 1, j):
                    dp[i][j] = min(
                        dp[i][j],
                        cuts[j] - cuts[i] + dp[i][mid] + dp[mid][j]
                    )

        return dp[0][m + 1]
