class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        previousMax = groupMax = 0
        previousBits = -1
        for x in nums:
            bits = x.bit_count()
            if bits != previousBits:
                previousMax = max(previousMax, groupMax)
                groupMax = x
                previousBits = bits
            else:
                groupMax = max(groupMax, x)
            if x < previousMax:
                return False
        return True
