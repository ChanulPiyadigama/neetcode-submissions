# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        else:
            if self.subRootCheck(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def subRootCheck(self, root, subroot):
        if not root and not subroot:
            return True
        elif not root or not subroot:
            return False
        elif root.val != subroot.val:
            return False
        return self.subRootCheck(root.left, subroot.left) and self.subRootCheck(root.right, subroot.right)