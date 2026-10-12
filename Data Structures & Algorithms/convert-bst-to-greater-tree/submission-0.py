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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0
        cur = root

        while cur:
            if cur.right:
                prev = cur.right
                while prev.left and prev.left != cur:
                    prev = prev.left

                if not prev.left:
                    prev.left = cur
                    cur = cur.right
                else:
                    prev.left = None
                    curSum += cur.val
                    cur.val = curSum
                    cur = cur.left
            else:
                curSum += cur.val
                cur.val = curSum
                cur = cur.left

        return root
        