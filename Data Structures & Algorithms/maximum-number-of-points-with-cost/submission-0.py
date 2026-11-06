class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        prev = points[0]

        for r in range(1, ROWS):
            cur = [0] * COLS
            cur[0] = prev[0]
            for c in range(1, COLS):
                cur[c] = max(prev[c], cur[c - 1] - 1)

            rightMax = prev[COLS - 1]
            for c in range(COLS - 2, -1 , -1):
                rightMax = max(prev[c], rightMax - 1)
                cur[c] = max(cur[c], rightMax) + points[r][c]

            cur[COLS - 1] += points[r][COLS - 1]
            prev = cur

        return max(prev)