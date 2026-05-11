class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = set()
        noIslands = 0
        
        def dfs(p):
            r, c = p
            if (
                r < 0 or r >= len(grid) or
                c < 0 or c >= len(grid[0]) or
                (r, c) in islands or
                grid[r][c] == '0'
            ):
                return
            islands.add((r, c))
            dfs((r - 1, c))
            dfs((r + 1, c))
            dfs((r, c - 1))
            dfs((r, c + 1))

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != "0" and (r, c) not in islands:
                    noIslands += 1
                    dfs((r, c))
        
        return noIslands
