class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap=[];total=0;answer=0
        for threshold,value in sorted(zip(nums2,nums1),reverse=True):
            heapq.heappush(heap,value);total+=value
            if len(heap)>k:total-=heapq.heappop(heap)
            if len(heap)==k:answer=max(answer,total*threshold)
        return answer

