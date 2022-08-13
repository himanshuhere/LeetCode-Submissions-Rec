#time kind of hardto find as there are 9^(n*2) but thats worst that would not happend many times dur to prunning bcs of isvalid case

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
    
        def solve():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        for c in range(1, 10):
                            if isvalid(i, j, c):
                                board[i][j] = str(c)
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True                 #base condition when things end

        def isvalid(row, col, c):
            for i in range(9):
                if board[i][col] == str(c):
                    return False
                if board[row][i] == str(c):
                    return False
                if board[3*(row//3) + i//3][3*(col//3) + i%3] == str(c):
                    return False
            return True
        
        solve()

