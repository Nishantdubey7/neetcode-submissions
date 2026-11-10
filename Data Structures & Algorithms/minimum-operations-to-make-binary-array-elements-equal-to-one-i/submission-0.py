class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                answer += 1
                for j in range(i, i + 3): nums[j] ^= 1
        return answer if nums[-1] == nums[-2] == 1 else -1

