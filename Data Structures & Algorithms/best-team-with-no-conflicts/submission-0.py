class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages,scores))
        dp = []
        for i,(_,score) in enumerate(players):
            best = score
            for j in range(i):
                if players[j][1] <= score: best = max(best, dp[j] + score)
            dp.append(best)
        return max(dp)

