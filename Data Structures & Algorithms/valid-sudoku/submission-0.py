class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowc = {}
        colc = {}
        boxc = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    box_id = (r // 3) * 3 + (c // 3)

                    if r not in rowc: rowc[r] = {}
                    if c not in colc: colc[c] = {}
                    if box_id not in boxc: boxc[box_id] = {}

                    if val in rowc[r] or val in colc[c] or val in boxc[box_id]:
                        return False

                    rowc[r][val] = 1
                    colc[c][val] = 1
                    boxc[box_id][val] = 1

        return True