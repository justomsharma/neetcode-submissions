class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #  first create a set to store keys for rows, column, and box
        seen = set()

        # iterate through every row and column
        for r in range(9):
            for c in range(9):
                
                # calculate value, if value is empty then skip it
                value = board[r][c]
                if value == ".":
                    continue
                
                # calculate the keys now :
                row_key = ("row", r, value)
                column_key = ("col", c, value)
                box_key = ("box", r // 3, c // 3, value)

                # verify if these keys are already in our created set
                if row_key in seen or column_key in seen or box_key in seen:
                    return False
                
                # add the keys in set so on next check for the same row, or column, or the box, we can verify again : reusing this
                seen.add(row_key)
                seen.add(column_key)
                seen.add(box_key)

        # if everything passes then its a valid sudoku
        return True