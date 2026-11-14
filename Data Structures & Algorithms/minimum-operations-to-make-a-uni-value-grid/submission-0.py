class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = sorted(v for row in grid for v in row)
        target = values[len(values)//2]
        answer = 0
        for v in values:
            distance = abs(v-target)
            if distance % x: return -1
            answer += distance//x
        return answer

