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
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack = [(root1, root2)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 or not node2:
                if node1 != node2:
                    return False
                continue

            if node1.val != node2.val:
                return False

            if ((node1.left and node2.left and
                 node1.left.val == node2.left.val) or
                (not node1.left and not node2.left)
            ):
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            else:
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))

        return True
        