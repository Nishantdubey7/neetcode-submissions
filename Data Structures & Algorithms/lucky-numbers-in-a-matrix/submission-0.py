class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        for row in matrix:
            c = min(range(len(row)), key=lambda j: row[j])
            if all(other[c] <= row[c] for other in matrix):
                return [row[c]]
        return []

