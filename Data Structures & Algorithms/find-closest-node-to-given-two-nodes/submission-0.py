class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n=len(edges)
        def distances(start):
            d=[-1]*n;step=0
            while start!=-1 and d[start]==-1:
                d[start]=step;step+=1;start=edges[start]
            return d
        a,b=distances(node1),distances(node2);answer=-1;best=n+1
        for i in range(n):
            if a[i]!=-1 and b[i]!=-1 and max(a[i],b[i])<best:best=max(a[i],b[i]);answer=i
        return answer

