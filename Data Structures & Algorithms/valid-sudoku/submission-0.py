from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for r in range(9):
            seen = set()
            for c in range(9):
                cell = board[r][c]

                if cell == ".":
                    continue

                if cell in seen:
                    return False

                seen.add(cell)

        # Check columns
        for c in range(9):
            seen = set()
            for r in range(9):
                cell = board[r][c]

                if cell == ".":
                    continue

                if cell in seen:
                    return False

                seen.add(cell)

        # Check 3x3 boxes
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                seen = set()

                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        cell = board[r][c]

                        if cell == ".":
                            continue

                        if cell in seen:
                            return False

                        seen.add(cell)

        return True