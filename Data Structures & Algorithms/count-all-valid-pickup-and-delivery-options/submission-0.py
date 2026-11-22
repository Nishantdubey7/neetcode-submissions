class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1000000007
        dp = [0] * (n + 1)
        dp[0] = 1

        for picked in range(n + 1):
            for delivered in range(picked):
                dp[delivered + 1] = (
                    (dp[delivered + 1] +
                    (picked - delivered) * dp[delivered]) % MOD
                )

            if picked < n:
                next_dp = [0] * (n + 1)
                for delivered in range(picked + 1):
                    next_dp[delivered] = (
                        (next_dp[delivered] +
                        (n - picked) * dp[delivered]) % MOD
                    )
                dp = next_dp

        return dp[n]
