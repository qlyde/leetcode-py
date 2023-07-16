class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(heights, rows, cols, r, c, visited, prevHeight):
            if (
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                heights[r][c] < prevHeight
            ):
                return

            visited.add((r, c))
            dfs(heights, rows, cols, r - 1, c, visited, heights[r][c])
            dfs(heights, rows, cols, r + 1, c, visited, heights[r][c])
            dfs(heights, rows, cols, r, c - 1, visited, heights[r][c])
            dfs(heights, rows, cols, r, c + 1, visited, heights[r][c])

        rows, cols = len(heights), len(heights[0])

        pacificVisited = set()
        atlanticVisited = set()

        for r in range(rows):
            dfs(heights, rows, cols, r, 0, pacificVisited, heights[r][0])
            dfs(heights, rows, cols, r, cols - 1, atlanticVisited, heights[r][cols - 1])

        for c in range(cols):
            dfs(heights, rows, cols, 0, c, pacificVisited, heights[0][c])
            dfs(heights, rows, cols, rows - 1, c, atlanticVisited, heights[rows - 1][c])

        ret = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacificVisited and (r, c) in atlanticVisited:
                    ret.append([r, c])
        return ret

