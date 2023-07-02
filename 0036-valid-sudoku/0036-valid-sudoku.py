class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue

                if (
                    num in rows[row] or
                    num in cols[col] or
                    num in squares[(row // 3, col // 3)]
                ):
                    return False

                rows[row].add(num)
                cols[col].add(num)
                squares[(row // 3, col // 3)].add(num)
        return True
        