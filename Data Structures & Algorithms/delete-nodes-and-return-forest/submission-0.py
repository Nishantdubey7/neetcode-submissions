class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        deleted=set(to_delete);forest=[];stack=[(root,True)]
        while stack:
            node,is_root=stack.pop()
            if node is None:continue
            remove=node.val in deleted
            if is_root and not remove:forest.append(node)
            for child in (node.left,node.right):
                if child:stack.append((child,remove))
            if node.left and node.left.val in deleted:node.left=None
            if node.right and node.right.val in deleted:node.right=None
        return forest

