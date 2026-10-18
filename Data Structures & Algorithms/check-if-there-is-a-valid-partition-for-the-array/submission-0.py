class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(2, n + 1):
            dp[i] = dp[i-2] and nums[i-2] == nums[i-1]
            if i >= 3:
                same = nums[i-3] == nums[i-2] == nums[i-1]
                rising = nums[i-3] + 1 == nums[i-2] and nums[i-2] + 1 == nums[i-1]
                dp[i] |= dp[i-3] and (same or rising)
        return dp[n]

