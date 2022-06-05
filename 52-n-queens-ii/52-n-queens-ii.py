class Solution:
    def totalNQueens(self, n: int) -> int:
        #could be easily solve in using same n queens 1 sol and return len of output rather the list but that is n! this cud be done in n or more maybe but not n!
        board = [['.' for i in range(n)] for i in range(n)] #fill board with .
        
        output = []
        # - - -
        def isSafe(board, row, col):
            #check on left side of row
            for i in range(col):
                if board[row][i] == 'Q':
                    return False
            
            #check on upper left diagonal
            for i, j in zip(range(row,-1,-1),range(col,-1,-1)):
                if board[i][j] == 'Q':
                    return False
                
            #check on lower left diagonal
            for i,j in zip(range(row,n),range(col,-1,-1)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        # - - - 
        def solve(board, col):
            #base case if all cols are processed
            if col >= n:
                out = []
                for row in board:
                    out.append(''.join(row))
                output.append(out[:])
                return True
            
            
            for row in range(n):
                if isSafe(board, row, col):
                    board[row][col] = 'Q'
                    solve(board, col+1)
                    board[row][col] = '.'
            
            return False
        # - - -
        
        solve(board, 0)
        return len(output)