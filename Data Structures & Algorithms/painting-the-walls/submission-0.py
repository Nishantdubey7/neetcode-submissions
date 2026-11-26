class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [float("inf")] * (n + 2)
        dp[0] = 0

        for i in range(n):
            for remain in range(n, 0, -1):
                paint = cost[i] + dp[max(remain - 1 - time[i], 0)]
                dp[remain] = min(paint, dp[remain])

        return dp[n]
