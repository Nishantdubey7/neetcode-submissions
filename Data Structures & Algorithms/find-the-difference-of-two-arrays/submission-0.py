class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        numSet1, numSet2 = set(nums1), set(nums2)
        return [list(numSet1 - numSet2), list(numSet2 - numSet1)]
        