class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = sum(nums)
        inside = sum(nums[:k])
        best = inside
        for start in range(1, len(nums)):
            inside += nums[(start + k - 1) % len(nums)] - nums[start - 1]
            best = max(best, inside)
        return k - best
