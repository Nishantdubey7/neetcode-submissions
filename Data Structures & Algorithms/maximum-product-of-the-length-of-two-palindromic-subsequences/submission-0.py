class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        limit = 1 << n
        pal = [0] * limit
        for mask in range(1,limit):
            word = "".join(s[i] for i in range(n) if mask >> i & 1)
            if word == word[::-1]: pal[mask] = len(word)
        best = pal.copy()
        for bit in range(n):
            for mask in range(limit):
                if mask >> bit & 1: best[mask] = max(best[mask],best[mask ^ (1 << bit)])
        return max(pal[mask] * best[(limit-1)^mask] for mask in range(limit))


