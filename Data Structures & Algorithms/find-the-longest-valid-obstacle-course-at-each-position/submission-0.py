import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res = []
        dp = [10**8] * (len(obstacles) + 1)

        for num in obstacles:
            index = bisect.bisect(dp, num)
            res.append(index + 1)
            dp[index] = num

        return res
