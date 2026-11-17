class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n, m = len(target), len(words[0])

        cnt = [[0] * 26 for _ in range(m)]
        for word in words:
            for i, c in enumerate(word):
                cnt[i][ord(c) - ord('a')] += 1

        dp = [0] * (m + 1)
        dp[m] = 1

        for i in range(n, -1, -1):
            nxt = 1 if i == n - 1 else 0
            for k in range(m - 1, -1, -1):
                cur = dp[k]
                dp[k] = dp[k + 1]
                if i < n:
                    c = ord(target[i]) - ord('a')
                    dp[k] = (dp[k] + cnt[k][c] * nxt) % MOD
                nxt = cur
            dp[m] = 0

        return dp[0]