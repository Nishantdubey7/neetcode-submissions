class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    bit = 1 << (int(board[r][c]) - 1)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + c // 3] |= bit

        def dfs(i):
            if i == len(empty):
                return True

            best, bestCnt = i, 10
            for j in range(i, len(empty)):
                r, c = empty[j]
                used = rows[r] | cols[c] | boxes[(r // 3) * 3 + c // 3]
                cnt = 9 - bin(used).count("1")
                if cnt < bestCnt:
                    best, bestCnt = j, cnt
                    if cnt <= 1:
                        break
            empty[i], empty[best] = empty[best], empty[i]

            r, c = empty[i]
            b = (r // 3) * 3 + c // 3
            used = rows[r] | cols[c] | boxes[b]
            for d in range(1, 10):
                bit = 1 << (d - 1)
                if used & bit:
                    continue
                board[r][c] = str(d)
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit
                if dfs(i + 1):
                    return True
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit
            board[r][c] = "."
            return False

        dfs(0)

