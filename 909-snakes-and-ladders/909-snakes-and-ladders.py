class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def numToPos(num):
            r, c = (num-1)//n, (num-1)%n
            if r % 2 == 0:
                return n-1-r, c
            else:
                return n-1-r, n-1-c
            
        vis = set()
        q = deque()
        q.append((1, 0))
        vis.add(1)
        
        while q:
            num, moves = q.popleft()
            r, c = numToPos(num)
            
            if board[r][c] != -1:       #update num if snake or ladder
                num = board[r][c]
                
            if num == n*n:
                return moves
            
            for i in range(1, 7):
                newnum = num + i
                if newnum not in vis:
                    vis.add(newnum)
                    q.append((newnum, moves + 1))
        return -1