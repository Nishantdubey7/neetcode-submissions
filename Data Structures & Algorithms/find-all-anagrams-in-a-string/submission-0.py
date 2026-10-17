class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, window = [0]*26, [0]*26
        for c in p: need[ord(c)-97] += 1
        answer = []
        for i,c in enumerate(s):
            window[ord(c)-97] += 1
            if i >= len(p): window[ord(s[i-len(p)])-97] -= 1
            if i+1 >= len(p) and window == need: answer.append(i+1-len(p))
        return answer

