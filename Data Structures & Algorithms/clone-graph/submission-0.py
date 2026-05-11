"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        nodes = {}

        def dfs(current):
            if current in nodes:
                return nodes[current]
            
            clone = Node(current.val)
            nodes[current] = clone

            for node in current.neighbors:
                clone.neighbors.append(dfs(node))

            return clone 
        return dfs(node)
