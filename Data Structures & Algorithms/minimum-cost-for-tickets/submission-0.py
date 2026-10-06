class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp7, dp30 = deque(), deque()
        dp = 0

        for d in days:
            while dp7 and dp7[0][0] + 7 <= d:
                dp7.popleft()

            while dp30 and dp30[0][0] + 30 <= d:
                dp30.popleft()

            dp7.append([d, dp + costs[1]])
            dp30.append([d, dp + costs[2]])
            dp = min(dp + costs[0], dp7[0][1], dp30[0][1])

        return dp
        