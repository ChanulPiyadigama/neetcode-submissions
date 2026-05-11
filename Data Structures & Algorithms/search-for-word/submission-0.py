from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w = []
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        found = False
        rows, cols = len(board), len(board[0])

        def visit(newRow, newCol):
            visited[newRow][newCol] = True
            w.append(board[newRow][newCol])
            dfs(newRow, newCol)
            w.pop()
            visited[newRow][newCol] = False

        def dfs(row, col):
            nonlocal found
            if found:
                return
            if len(w) == len(word):
                if "".join(w) == word:
                    found = True
                return 

            # up
            if row > 0 and not visited[row - 1][col]:
                visit(row - 1, col)

            # right
            if col < cols - 1 and not visited[row][col + 1]:
                visit(row, col + 1)

            # down
            if row < rows - 1 and not visited[row + 1][col]:
                visit(row + 1, col)

            # left
            if col > 0 and not visited[row][col - 1]:
                visit(row, col - 1)

        # Start DFS from every cell in the board
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # small optimization
                    visit(i, j)
                    if found:
                        return True

        return False
