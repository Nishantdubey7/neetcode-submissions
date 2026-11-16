class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n + 1)

        for cur_goal in range(1, goal + 1):
            prev = 1 if cur_goal == 1 else 0
            for old_songs in range(1, n + 1):
                res = (prev * (n - old_songs + 1)) % mod
                if old_songs > k:
                    res = (res + dp[old_songs] * (old_songs - k)) % mod
                prev = dp[old_songs]
                dp[old_songs] = res

        return dp[n]
