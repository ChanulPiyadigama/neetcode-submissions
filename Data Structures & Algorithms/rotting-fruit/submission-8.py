from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        freshFruit = 0
        mins = 0

        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if val == 2:
                    queue.append((r,c))
                elif val == 1:
                    freshFruit += 1
        
        if freshFruit == 0:
            return 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and freshFruit > 0:
            mins += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    freshFruit -= 1
                    queue.append((nr, nc))
        return mins if freshFruit == 0 else -1