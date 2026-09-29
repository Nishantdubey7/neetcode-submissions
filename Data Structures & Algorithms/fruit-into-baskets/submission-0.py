class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l = 0
        fruit1_lastIdx = 0
        fruit2_lastIdx = -1
        fruit1 = fruits[0]
        fruit2 = -1
        total = res = 1

        for r in range(len(fruits)):
            f = fruits[r]
            if f == fruit1:
                total += 1
                fruit1_lastIdx = r
            elif f == fruit2 or fruit2 == -1:
                total += 1
                fruit2_lastIdx = r
                fruit2 = f
            else:
                if fruit2_lastIdx == min(fruit1_lastIdx, fruit2_lastIdx):
                    fruit1_lastIdx, fruit2_lastIdx = fruit2_lastIdx, fruit1_lastIdx
                    fruit1, fruit2 = fruit2, fruit1

                total -= (fruit1_lastIdx - l + 1)
                l = fruit1_lastIdx + 1
                fruit1 = f
                fruit1_lastIdx = r
            res = max(res, r - l + 1)

        return res
        