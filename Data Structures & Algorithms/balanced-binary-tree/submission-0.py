# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0

            leftChildDepth = dfs(root.left)
            if leftChildDepth == -1:
                return -1
            rightChildDepth = dfs(root.right)
            if rightChildDepth == -1:
                return -1

            if abs(leftChildDepth - rightChildDepth) > 1:
                return -1

            return 1 + max(leftChildDepth,rightChildDepth)
        return dfs(root) != -1
                