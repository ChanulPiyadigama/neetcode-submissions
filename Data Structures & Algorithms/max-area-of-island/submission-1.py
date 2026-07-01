class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        def dfs(r: int, c: int) -> int:
            # Base case: out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
                
            # Sink the land to mark as visited
            grid[r][c] = 0
            
            # Return 1 (current cell) + area of all 4 adjacent directions
            return (1 + 
                    dfs(r + 1, c) + 
                    dfs(r - 1, c) + 
                    dfs(r, c + 1) + 
                    dfs(r, c - 1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Update max_area if the current island is larger
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area
