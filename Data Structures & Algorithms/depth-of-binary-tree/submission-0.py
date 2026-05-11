# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        return self.maxDepthRec(root, depth)

    def maxDepthRec(self, root, depth):
        if not root:
            return depth 
        else:
            depth+=1
            return max(
                self.maxDepthRec(root.left, depth),
                self.maxDepthRec(root.right, depth)
            )
                