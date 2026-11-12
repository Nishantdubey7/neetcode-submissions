class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        def build(count):
            if count==1:return [TreeNode(0)]
            answer=[]
            for left_count in range(1,count-1,2):
                for left in build(left_count):
                    for right in build(count-1-left_count):answer.append(TreeNode(0,left,right))
            return answer
        return build(n) if n%2 else []

