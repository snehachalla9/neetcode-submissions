# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issametree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return (issametree(p.left, q.left) and
            issametree(p.right, q.right))
        stack=[root]
        while stack:
            node=stack.pop()
            if issametree(node,subRoot):
                return True
            if node:
                stack.append(node.left)
                stack.append(node.right)
        return False




        