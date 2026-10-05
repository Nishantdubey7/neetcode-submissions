class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        queue = deque()
        for i in range(1, n):
            if indegree[i] == 1:
                queue.append(i)
                indegree[i] = 0

        time = [0] * n
        while queue:
            node = queue.popleft()
            for nei in adj[node]:
                if indegree[nei] <= 0:
                    continue

                indegree[nei] -= 1
                if hasApple[node] or time[node] > 0:
                    time[nei] += time[node] + 2
                if indegree[nei] == 1 and nei != 0:
                    queue.append(nei)

        return time[0]
        