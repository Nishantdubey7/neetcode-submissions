class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        counts = [0] * 26
        for c in s:
            counts[ord(c) - 97] += 1
        return sum(x % 2 for x in counts) <= k
