class Solution:
    def isRobotBounded(self, ins: str) -> bool:
              #north, south, west, east
              #up, back, down, front
        dir = [[0,1], [-1,0],[0,-1],[1,0]]
        di = 0  #north up facing
        x,y = 0,0   #initial origin
        
        for i in ins:
            if i == 'L':
                di = (di+1)%4
            elif i == 'R':
                di = (di-1)%4
            else:
                x += dir[di][0]
                y += dir[di][1]
        
        #check back in origin with north face
        return x==0 and y==0 or di!=0