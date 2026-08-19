class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        store = [[n + 1] * 26 for _ in range(n)]
        store[n - 1][ord(s[n - 1]) - ord('a')] = n - 1

        for i in range(n - 2, -1, -1):
            store[i] = store[i + 1][:]
            store[i][ord(s[i]) - ord('a')] = i

        i, j = 0, 0
        while i < n and j < m:
            if store[i][ord(t[j]) - ord('a')] == n + 1:
                break

            i = store[i][ord(t[j]) - ord('a')] + 1
            j += 1

        return m - j