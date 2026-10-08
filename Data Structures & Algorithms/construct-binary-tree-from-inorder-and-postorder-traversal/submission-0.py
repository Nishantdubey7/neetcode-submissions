# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postIdx = inIdx = len(postorder) - 1
        def dfs(limit):
            nonlocal postIdx, inIdx
            if postIdx < 0:
                return None
            if inorder[inIdx] == limit:
                inIdx -= 1
                return None

            root = TreeNode(postorder[postIdx])
            postIdx -= 1
            root.right = dfs(root.val)
            root.left = dfs(limit)
            return root
        return dfs(float('inf'))
        