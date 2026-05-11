from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1 
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
        if fresh == 0:
            return 0
                

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        maxDis = -1
        rotten= 0
        while queue:
            r, c = queue.popleft()
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if(
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    grid[nr][nc] == 1
                ):
                    grid[nr][nc] = grid[r][c]+1
                    maxDis = max(maxDis, grid[nr][nc])
                    queue.append((nr,nc))
                    rotten+=1
        
        return maxDis-2 if rotten == fresh else -1

                
        