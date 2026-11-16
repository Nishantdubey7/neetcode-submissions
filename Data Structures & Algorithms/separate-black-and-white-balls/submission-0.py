class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = steps = 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                steps += ones
        return steps

