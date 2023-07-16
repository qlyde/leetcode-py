class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, rows, cols, r, c, visited):
            if (
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                board[r][c] != "O"
            ):
                return

            visited.add((r, c))
            board[r][c] = "."

            dfs(board, rows, cols, r - 1, c, visited)
            dfs(board, rows, cols, r + 1, c, visited)
            dfs(board, rows, cols, r, c - 1, visited)
            dfs(board, rows, cols, r, c + 1, visited)

        # dfs from edge O's
        rows, cols = len(board), len(board[0])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if r in (0, rows - 1) or c in (0, cols - 1):
                    dfs(board, rows, cols, r, c, visited)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    board[r][c] = "O"

        return board
