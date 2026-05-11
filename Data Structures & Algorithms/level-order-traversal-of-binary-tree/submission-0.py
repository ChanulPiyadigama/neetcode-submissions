# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodesAtLevels= []
        depth = 0
        def levelOrderRec(node, depth):
            if not node:
                return
            if len(nodesAtLevels) < depth+1:
                nodesAtLevels.append([])
            nodesAtLevels[depth].append(node.val)

            levelOrderRec(node.left, depth+1)
            levelOrderRec(node.right, depth+1)

            return
        levelOrderRec(root, depth)
        return nodesAtLevels
