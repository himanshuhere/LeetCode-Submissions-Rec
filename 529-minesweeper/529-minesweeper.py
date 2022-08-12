#Let's undertstand the flow in laymans term bruh. (What i understand baki dekh lena clear karke)
# If b[i][j] is M, game is over make that X and return
# Else (If E)
#     Check its 8 adjacent, and if any M present count them and fill that digit here in current cell and leave the game
#     If no M present on adjacents, put B here and recursively go on clicking every adjacent

#We ll be using smart DFS see

class Solution:
    def getAdjacentMines(self, board, x, y): 
        numMines=0
        for r in range(x-1, x+2): 
            for c in range(y-1, y+2):   #you need to put one condition for [x, y] that r!=x and c!=y, bcs out of 9 pairs, one would again be same cell, here it is fine as cureent cell is B, else take care
                if r >= 0 and r < len(board) and c >= 0 and c < len(board[r]) and board[r][c] == "M":
                    numMines += 1
        return numMines
    
    def updateBoard(self, board, click): 
        x, y = click
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        else:
            numMines = self.getAdjacentMines(board, x, y)
            if numMines > 0:
                board[x][y]= str(numMines)
            else:
                board[x][y] = "B"
                for r in range(x-1, x+2):
                    for c in range(y-1, y+2):
                        #you need to put one condition for [x, y] that r!=x and c!=y, bcs out of 9 pairs, one would again be same cell, here it is fine as cureent cell is B, else take care
                        if r >= 0 and r < len(board) and c >= 0 and c < len(board[r]) and board[r][c] != "B":
                            self.updateBoard(board, [r, c])
        return board