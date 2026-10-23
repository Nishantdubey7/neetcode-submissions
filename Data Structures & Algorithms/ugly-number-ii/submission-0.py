class Solution:
    def nthUglyNumber(self, n: int) -> int:
        values = [1] * n
        a = b = c = 0
        for i in range(1, n):
            value = min(values[a] * 2, values[b] * 3, values[c] * 5)
            values[i] = value
            if values[a] * 2 == value: a += 1
            if values[b] * 3 == value: b += 1
            if values[c] * 5 == value: c += 1
        return values[-1]

