class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        available=[0]*26
        for c in letters:available[ord(c)-97]+=1
        answer=0
        for mask in range(1<<len(words)):
            used=[0]*26;total=0
            for i,word in enumerate(words):
                if mask>>i&1:
                    for c in word:at=ord(c)-97;used[at]+=1;total+=score[at]
            if all(used[i]<=available[i] for i in range(26)):answer=max(answer,total)
        return answer

