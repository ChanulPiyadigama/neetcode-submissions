# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0  # height of null node is 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            # update max_diameter at this node
            self.max_diameter = max(self.max_diameter, left + right)
            
            # height of this node = max height of subtrees + 1
            return 1 + max(left, right)

        dfs(root)
        return self.max_diameter
        