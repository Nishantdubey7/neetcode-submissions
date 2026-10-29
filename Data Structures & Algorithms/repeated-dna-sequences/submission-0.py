class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set(); repeated = set()
        for i in range(len(s)-9):
            word = s[i:i+10]
            if word in seen: repeated.add(word)
            seen.add(word)
        return list(repeated)
