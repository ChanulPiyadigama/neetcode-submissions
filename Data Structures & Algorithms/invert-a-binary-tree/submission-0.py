# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.invertTreeRec(root)
        return root
    
    def invertTreeRec(self, root):
        if not root.left and not root.right:
            return 
        elif root.left and  not root.right:
            root.right = root.left
            root.left = None
            self.invertTreeRec(root.right)
        elif not root.left and root.right:
            root.left = root.right
            root.right = None
            self.invertTreeRec(root.left)
        else:
            root.left, root.right = root.right, root.left
            self.invertTreeRec(root.right)
            self.invertTreeRec(root.left)
        return