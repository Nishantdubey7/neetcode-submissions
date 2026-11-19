class DSU:
    def __init__(self, n):
        self.Parent = list(range(n))
        self.Components = n

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, parent, child):
        parentRoot = self.find(parent)
        childRoot = self.find(child)
        if childRoot != child or parentRoot == childRoot:
            return False

        self.Components -= 1
        self.Parent[childRoot] = parentRoot
        return True

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        dsu = DSU(n)

        for parent in range(n):
            for child in (leftChild[parent], rightChild[parent]):
                if child == -1:
                    continue
                if not dsu.union(parent, child):
                    return False

        return dsu.Components == 1