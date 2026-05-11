# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = []
        def goodNodesRec(node, maxVal):
            if not node:
                return 
            if node.val >= maxVal:
                goodNodes.append(node)
            goodNodesRec(node.left, max(maxVal, node.val))
            goodNodesRec(node.right, max(maxVal, node.val))
            return
        goodNodesRec(root, -101)
        return len(goodNodes)
