class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        best = {}
        answer = 1
        for word in sorted(words, key=len):
            length = 1
            for i in range(len(word)):
                length = max(length, 1 + best.get(word[:i] + word[i+1:], 0))
            best[word] = length
            answer = max(answer, length)
        return answer

