class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dummy = [[0]*(len(board[0])+2) for _ in range(len(board)+2)]
        for i in range(1, len(dummy)-1):
            for j in range(1, len(dummy[0])-1):
                dummy[i][j] = board[i-1][j-1]
        
        #print(dummy)
        
        def neiCounts(i, j):
            return dummy[i][j-1] + dummy[i][j+1] + dummy[i-1][j] + dummy[i+1][j] + dummy[i+1][j-1] + dummy[i+1][j+1] + dummy[i-1][j-1] + dummy[i-1][j+1]
                
            
        for i in range(1, len(dummy)-1):
            for j in range(1, len(dummy[0])-1):
                nc = neiCounts(i, j)
                if dummy[i][j] == 1 and nc < 2:
                    board[i-1][j-1] = 0
                elif dummy[i][j] == 1 and (nc == 2 or nc == 3):
                    board[i-1][j-1] = 1
                elif dummy[i][j] == 1 and nc > 3:
                    board[i-1][j-1] = 0
                elif dummy[i][j] == 0 and nc == 3:
                    board[i-1][j-1] = 1
        return board