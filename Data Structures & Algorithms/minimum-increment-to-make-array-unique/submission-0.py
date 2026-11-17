class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        answer = 0
        nextValue = 0
        for x in sorted(nums):
            chosen = max(x,nextValue)
            answer += chosen-x
            nextValue = chosen+1
        return answer
