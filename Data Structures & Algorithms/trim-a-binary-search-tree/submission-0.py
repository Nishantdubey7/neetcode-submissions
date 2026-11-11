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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root and not low<=root.val<=high:root=root.right if root.val<low else root.left
        node=root
        while node:
            while node.left and node.left.val<low:node.left=node.left.right
            node=node.left
        node=root
        while node:
            while node.right and node.right.val>high:node.right=node.right.left
            node=node.right
        return root
