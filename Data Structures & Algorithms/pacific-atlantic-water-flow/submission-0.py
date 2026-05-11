class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # Start DFS from all Pacific-bordering cells
        for c in range(cols):
            dfs(0, c, pacific_reachable)      # Top row (Pacific)
            dfs(rows - 1, c, atlantic_reachable)  # Bottom row (Atlantic)

        for r in range(rows):
            dfs(r, 0, pacific_reachable)      # Left column (Pacific)
            dfs(r, cols - 1, atlantic_reachable)  # Right column (Atlantic)

        # Result = intersection of both sets
        return list(pacific_reachable & atlantic_reachable)
