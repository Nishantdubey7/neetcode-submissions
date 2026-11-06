class Solution:
    def maxScore(self, nums: List[int]) -> int:
        from math import gcd
        n = len(nums); size = 1 << n
        g = [[gcd(x,y) for y in nums] for x in nums]
        dp = [0]*size
        for mask in range(size):
            used = mask.bit_count()
            if used % 2: continue
            operation = used//2+1
            for i in range(n):
                if mask >> i & 1: continue
                for j in range(i+1,n):
                    if mask >> j & 1: continue
                    nxt = mask | 1<<i | 1<<j
                    dp[nxt] = max(dp[nxt],dp[mask]+operation*g[i][j])
        return dp[-1]
