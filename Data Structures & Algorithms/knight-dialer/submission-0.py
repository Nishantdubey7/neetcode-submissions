class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        counts = [1]*10
        for _ in range(n-1):
            following = [0]*10
            for digit in range(10):
                for destination in moves[digit]: following[destination] = (following[destination]+counts[digit])%1000000007
            counts = following
        return sum(counts)%1000000007

