class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        #min nikaal lete valids me but fir min kai sare ho sakte aur unme se bhi small index dena hai so heap
        #min heap
        # h = []
        # for x1,y1 in points:
        #     if x1 != x and y1 != y:  continue    #invalid
        #     dist = abs(x-x1) + abs(y-y1)
        #     heappush(h, ((dist, x1) , [x1,y1]))
        # print(h)
        # if h:
        #     pack, coord = heappop(h)
        #     if coord == [x, y]: 
        #         return 0
        #     return abs(coord[0]-x)
        # return -1
        
        #sab farxi hai no heap weap, see if any of one sharing same coordinates. means diff of x-x1 or y-y1 koi bhi ek or do will be zero so say dx=x-x1 and dy=y-y1, so dx*dy == 0 right
        #bas mini lo aur dx*dy==0 and abs(dx-dy) < mini, so update mini and keep coordinate also
        
        ans = -1       
        smallest = math.inf
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            
            dx = x - x1
            dy = y - y1
            if dx*dy == 0 and abs(dx+dy) < smallest:
                smallest = abs(dx+dy)
                ans = i
        return ans
        
        
        
            
            
    