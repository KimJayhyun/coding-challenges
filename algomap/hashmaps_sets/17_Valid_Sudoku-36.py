from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row_set = set()
            col_set = set()

            for j in range(9):
                row_cell = board[i][j]
                col_cell = board[j][i]

                if not row_cell == ".":
                    if row_cell in row_set:
                        return False

                    row_set.add(row_cell)

                if not col_cell == ".":
                    if col_cell in col_set:
                        return False

                    col_set.add(col_cell)

        for i, j in [
            (0, 0),
            (0, 3),
            (0, 6),
            (3, 0),
            (3, 3),
            (3, 6),
            (6, 0),
            (6, 3),
            (6, 6),
        ]:
            seem = set()
            for dx, dy in [(i, j) for i in range(3) for j in range(3)]:
                cell = board[i + dx][j + dy]

                if cell == ".":
                    continue

                if cell in seem:
                    return False

                seem.add(cell)

        return True
