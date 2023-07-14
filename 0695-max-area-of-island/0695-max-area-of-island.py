class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, rows, cols, row, col, visited):
            area = 0
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()

                if (
                    r not in range(rows) or
                    c not in range(cols) or
                    (r, c) in visited or
                    grid[r][c] == 0
                ):
                    continue

                visited.add((r, c))
                area += 1

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    stack.append((r + dr, c + dc))
            return area

        ret = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(grid, rows, cols, r, c, visited)
                    ret = max(ret, area)
        return ret
        
