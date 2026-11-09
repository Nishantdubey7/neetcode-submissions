class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        up, down = [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]: up[i] = max(up[i], up[j] + 1)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] < nums[i]: down[i] = max(down[i], down[j] + 1)
        return n - max(up[i] + down[i] - 1 for i in range(n) if up[i] > 1 and down[i] > 1)
