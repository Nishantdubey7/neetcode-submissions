class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = []
        dots = 0
        R = False

        for d in dominoes:
            if d == '.':
                dots += 1
            elif d == 'R':
                if R:
                    res.append('R' * (dots + 1))
                elif dots > 0:
                    res.append('.' * dots)
                dots = 0
                R = True
            else:
                if R:
                    res.append('R')
                    if dots > 0:
                        res.append('R' * (dots // 2))
                        if (dots % 2) != 0:
                            res.append('.')
                        res.append('L' * (dots // 2))
                    res.append('L')
                    R, dots = False, 0
                else:
                    res.append('L' * (dots + 1))
                    dots = 0

        if R:
            res.append('R' * (dots + 1))
        else:
            res.append('.' * dots)

        return ''.join(res)


