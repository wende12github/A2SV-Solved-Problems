class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows_map = defaultdict(set)
        cols_map = defaultdict(set)
        boxs_map = defaultdict(set)

        def dfsBacktrack(row, col):
            if row == 9:
                return True
            
            if board[row][col] != ".":
                if col + 1 < 9:
                    return dfsBacktrack(row, col + 1)
                else:
                    return dfsBacktrack(row + 1, 0)
                    
            for num in '123456789':
                sub_s = (row // 3) * 3 + (col // 3)
                if num in rows_map[row] or num in cols_map[col] or num in boxs_map[sub_s]:
                    continue

                board[row][col] = num
                rows_map[row].add(num)
                cols_map[col].add(num)
                boxs_map[sub_s].add(num)

                result = dfsBacktrack(row, col + 1) if col < 8 else dfsBacktrack(row + 1, 0)

                if result:
                    return True

                board[row][col] = "."
                rows_map[row].remove(num)
                cols_map[col].remove(num)
                boxs_map[sub_s].remove(num)

            return False
        
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n != ".":
                    rows_map[i].add(n)
                    cols_map[j].add(n)
                    boxs_map[(i // 3) * 3 + (j // 3)].add(n)
                 
        dfsBacktrack(0, 0)

