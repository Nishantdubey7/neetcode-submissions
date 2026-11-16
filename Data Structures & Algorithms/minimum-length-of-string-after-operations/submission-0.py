class Solution:
    def minimumLength(self, s: str) -> int:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - 97] += 1
        return sum(1 if n % 2 else 2 for n in counts if n)
