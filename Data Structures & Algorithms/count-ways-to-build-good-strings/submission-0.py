class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1]+[0]*high; answer = 0
        for length in range(1,high+1):
            if length >= zero: dp[length] += dp[length-zero]
            if length >= one: dp[length] += dp[length-one]
            dp[length] %= 1000000007
            if length >= low: answer = (answer+dp[length])%1000000007
        return answer

