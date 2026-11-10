class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2: return False
        low = high = 0
        for c, fixed in zip(s,locked):
            if fixed == "0": low -= 1; high += 1
            elif c == "(": low += 1; high += 1
            else: low -= 1; high -= 1
            if high < 0: return False
            low = max(low,0)
        return low == 0

