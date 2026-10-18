class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        letters = [ord(c)-97 for c in target]; n = len(letters); full = (1<<n)-1
        counts = []
        for word in stickers:
            row = [0]*26
            for c in word: row[ord(c)-97] += 1
            counts.append(row)
        dp = [16]*(full+1); dp[0] = 0
        for mask in range(full):
            if dp[mask] == 16: continue
            first = next(j for j in range(n) if not mask>>j&1)
            for row in counts:
                if row[letters[first]] == 0: continue
                left = row[:]; nxt = mask
                for j,c in enumerate(letters):
                    if not nxt>>j&1 and left[c]: nxt |= 1<<j; left[c] -= 1
                dp[nxt] = min(dp[nxt],dp[mask]+1)
        return -1 if dp[full]==16 else dp[full]

