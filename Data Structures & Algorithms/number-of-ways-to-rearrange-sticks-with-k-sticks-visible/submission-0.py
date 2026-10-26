class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = [1] + [0] * k
        for size in range(1,n+1):
            for visible in range(k,0,-1): dp[visible] = (dp[visible-1] + (size-1)*dp[visible]) % 1000000007
            dp[0] = 0
        return dp[k]

