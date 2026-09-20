class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) 

        row_len = len(board)
        col_len = len(board[0])
        for i in range(row_len):
            for j in range(col_len):
                val = board[i][j]
                if val == ".":
                    continue
                
                ##Check if it exists in rows
                if val in rows[i]:
                    return False
                rows[i].add(val)

                ##Check Col
                if val in cols[j]:
                    return False
                cols[j].add(val)

                ##Check Grid
                grid_index = (i//3, j//3)
                if val in squares[grid_index]:
                    return False
                squares[grid_index].add(val)

        return True 