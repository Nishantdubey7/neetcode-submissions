class Solution:
    def minSwaps(self, s: str) -> int:
        stackSize = 0
        for c in s:
            if c == '[':
                stackSize += 1
            elif stackSize > 0:
                stackSize -= 1
        return (stackSize + 1) // 2
        