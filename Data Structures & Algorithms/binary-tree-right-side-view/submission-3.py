# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        results = []

        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # If it's the last node in the current level, it's visible from the right
                if i == level_size - 1:
                    results.append(node.val)
                
                # Standard BFS: push left first, then right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return results