class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = sum(1 << (ord(c) - ord('a')) for c in "aeiou")
        prefix = [0]
        for w in words:
            prefix.append(prefix[-1])
            if (1 << (ord(w[0]) - ord('a'))) & vowels and (1 << (ord(w[-1]) - ord('a'))) & vowels:
                prefix[-1] += 1
        return [prefix[r + 1] - prefix[l] for l, r in queries]
        