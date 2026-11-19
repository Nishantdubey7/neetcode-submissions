# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        stack = [(root, "")]
        res = None

        while stack:
            node, cur = stack.pop()
            cur = chr(ord('a') + node.val) + cur

            if not node.left and not node.right:
                res = min(res, cur) if res else cur

            if node.right:
                stack.append((node.right, cur))
            if node.left:
                stack.append((node.left, cur))

        return res
        