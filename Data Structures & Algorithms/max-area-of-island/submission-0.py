class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        foundIslands = set()
        maxArea = 0

        areaCurrIsland = 0
        def dfs(p):
            nonlocal areaCurrIsland
            r, c = p
            if (
                r < 0 or r >= len(grid) or
                c < 0 or c >= len(grid[0]) or
                (r, c) in foundIslands or
                grid[r][c] == 0
            ):
                return
            foundIslands.add((r, c))
            areaCurrIsland+=1
            dfs((r - 1, c))
            dfs((r + 1, c))
            dfs((r, c - 1))
            dfs((r, c + 1))
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and (r, c) not in foundIslands:
                    dfs((r, c))
                    maxArea = max(maxArea, areaCurrIsland)
                    areaCurrIsland = 0
        return maxArea