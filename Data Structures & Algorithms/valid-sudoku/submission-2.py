class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        grids = {}
        for i in range(9):
            rows[i] = set()
            cols[i] = set()
            grids[i] = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[i][j]
                grid = 3*(i // 3) + (j // 3)
                if cell == ".":
                    continue
                if cell in rows[i] or cell in cols[j] or cell in grids[grid]:
                    return False;
                rows[i].add(cell)
                cols[j].add(cell)
                grids[grid].add(cell)
        return True


