class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        firstIdx = [-1] * 26
        res = -1

        for i, c in enumerate(s):
            j = ord(c) - ord('a')
            if firstIdx[j] != -1:
                res = max(res, i - firstIdx[j] - 1)
            else:
                firstIdx[j] = i

        return res