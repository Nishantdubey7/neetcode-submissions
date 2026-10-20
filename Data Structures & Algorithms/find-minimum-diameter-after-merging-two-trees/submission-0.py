class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def diameter(edges):
            n=len(edges)+1
            if n==1:return 0
            graph=[[] for _ in range(n)];degree=[0]*n
            for u,v in edges:graph[u].append(v);graph[v].append(u);degree[u]+=1;degree[v]+=1
            leaves=[i for i in range(n) if degree[i]==1];head=0;remaining=n;depth=0
            while remaining>2:
                stop=len(leaves);remaining-=stop-head;depth+=2
                while head<stop:
                    u=leaves[head];head+=1
                    for v in graph[u]:
                        degree[v]-=1
                        if degree[v]==1:leaves.append(v)
            return depth+(remaining==2)
        a,b=diameter(edges1),diameter(edges2)
        return max(a,b,(a+1)//2+(b+1)//2+1)

        