class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph=[[] for _ in range(n+1)]
        for u,v in edges:graph[u].append(v);graph[v].append(u)
        best=[0]*(n+1)
        for start in range(1,n+1):
            dist=[-1]*(n+1);dist[start]=0;queue=[start];root=start;depth=0
            for u in queue:
                root=min(root,u);depth=max(depth,dist[u]+1)
                for v in graph[u]:
                    if dist[v]==-1:dist[v]=dist[u]+1;queue.append(v)
                    elif dist[v]%2==dist[u]%2:return -1
            best[root]=max(best[root],depth)
        return sum(best)

        