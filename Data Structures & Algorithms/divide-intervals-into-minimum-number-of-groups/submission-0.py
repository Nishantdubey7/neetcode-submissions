class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        starts = sorted(p[0] for p in intervals)
        ends = sorted(p[1] for p in intervals)
        j = answer = 0
        for i, start in enumerate(starts):
            while ends[j] < start:
                j += 1
            answer = max(answer, i - j + 1)
        return answer
