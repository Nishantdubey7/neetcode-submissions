class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10**9 + 7
        N = len(group)

        dp = [[0] * (minProfit + 1) for j in range(n + 2)]
        for j in range(n + 1):
            dp[j][minProfit] = 1

        for i in range(N - 1, -1, -1):
            for j in range(n, -1, -1):
                for p in range(minProfit + 1):
                    res = dp[j][p]
                    if j >= group[i]:
                        nxtP = min(profit[i] + p, minProfit)
                        res = (res + dp[j - group[i]][nxtP]) % mod
                    dp[j][p] = res

        return dp[n][0]