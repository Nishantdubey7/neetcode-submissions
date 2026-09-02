class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit = set()
        x, y = 0, 0
        visit.add(self.hash(x, y))

        for c in path:
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            elif c == 'W':
                x -= 1

            pos = self.hash(x, y)
            if pos in visit:
                return True
            visit.add(pos)

        return False

    def hash(self, x: int, y: int) -> int:
        return (x << 32) + y
        