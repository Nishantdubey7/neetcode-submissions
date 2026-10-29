class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [float(poured)]
        for r in range(query_row):
            nxt = [0.0]*(r+2)
            for c, amount in enumerate(row):
                excess = max(0.0, (amount-1)/2)
                nxt[c] += excess; nxt[c+1] += excess
            row = nxt
        return min(1.0, row[query_glass])
