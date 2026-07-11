class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []
        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue
                
                row_key = ("row", r, value)
                col_key = ("col", c, value)
                box_key = ("box", r // 3, c // 3, value)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.append(row_key)
                seen.append(col_key)
                seen.append(box_key)
        
        return True