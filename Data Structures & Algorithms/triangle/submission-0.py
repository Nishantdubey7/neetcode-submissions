class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[0][:]

        for row in range(1, n):
            nxtDp = [0] * len(triangle[row])
            nxtDp[0] = dp[0] + triangle[row][0]
            for col in range(1, len(triangle[row]) - 1):
                nxtDp[col] = triangle[row][col] + min(dp[col], dp[col - 1])
            nxtDp[-1] = dp[-1] + triangle[row][-1]
            dp = nxtDp

        return min(dp)
        