class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        queue = deque((r,c) for r in range(n) for c in range(n) if grid[r][c])
        if not queue or len(queue) == n*n:
            return -1
        distance = -1
        while queue:
            distance += 1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for rr,cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if 0 <= rr < n and 0 <= cc < n and grid[rr][cc] == 0:
                        grid[rr][cc] = 1
                        queue.append((rr,cc))
        return distance
