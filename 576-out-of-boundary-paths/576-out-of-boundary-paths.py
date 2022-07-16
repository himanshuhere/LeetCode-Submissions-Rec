class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = int(1e9+7)

        @lru_cache(None)
        def recursion(move, row, col):
            if row == m or row == -1 or col == n or col == -1:  #out of boundary, with atleast 0 moves here 
                return 1
            if move == 0:       #at any point move ends, call ends
                return 0
            
            move -= 1
            return (
                recursion(move, row, col + 1)
                + recursion(move, row, col - 1)
                + recursion(move, row - 1, col)
                + recursion(move, row + 1, col)
            ) % modulo
        
        return recursion(maxMove, startRow, startColumn)