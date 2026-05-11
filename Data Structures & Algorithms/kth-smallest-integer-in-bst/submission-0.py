# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = []

        def inOrderSearch(root):
            if not root:
                return 
            inOrderSearch(root.left)
            inOrder.append(root.val)
            inOrderSearch(root.right)
            return
        inOrderSearch(root)
        return inOrder[k-1]