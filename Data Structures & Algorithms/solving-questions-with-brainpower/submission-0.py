class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points, skip = questions[i]
            dp[i] = max(dp[i + 1], points + dp[min(n, i + skip + 1)])
        return dp[0]

