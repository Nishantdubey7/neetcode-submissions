class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        firstIndex = [-1] * 26
        lastIndex = [-1] * 26

        for i in range(len(s)):
            j = ord(s[i]) - ord('a')
            if firstIndex[j] == -1:
                firstIndex[j] = i
            lastIndex[j] = i

        res = 0
        for ends in range(26):
            if firstIndex[ends] == -1 or firstIndex[ends] == lastIndex[ends]:
                continue
            l, r = firstIndex[ends], lastIndex[ends]
            mask = 0
            for i in range(l + 1, r):
                c = ord(s[i]) - ord('a')
                if mask & (1 << c):
                    continue
                mask |= (1 << c)
                res += 1

        return res
        