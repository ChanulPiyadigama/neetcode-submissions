# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def IsSameTreeRec(p,q):
            if p and not q:
                return False
            elif not p and q:
                return False
            elif not p and not q:
                return True
            elif p.val != q.val:
                return False
            else:
                if not IsSameTreeRec(p.left, q.left) or not IsSameTreeRec(p.right, q.right):
                    return False
            return True
        return IsSameTreeRec(p,q)

            
        