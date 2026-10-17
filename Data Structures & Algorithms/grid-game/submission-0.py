class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top = sum(grid[0])
        bottom = 0
        answer = top
        for c in range(len(grid[0])):
            top -= grid[0][c]
            answer = min(answer, max(top, bottom))
            bottom += grid[1][c]
        return answer

