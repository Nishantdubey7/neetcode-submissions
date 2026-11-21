class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        answer = 1440 + minutes[0] - minutes[-1]
        for i in range(1, len(minutes)):
            answer = min(answer, minutes[i] - minutes[i - 1])
        return answer
