class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #sort on ending pos, shoot on first balloons ending pos, assuming that if end is sorted folowing baloons will be inside this cur end and now take care of start only. if cur shot pos is lesser than start then new arrow and update the arrow pos to its end else no new arrow so no new c++.
        
        
        points = sorted(points, key=lambda x:x[1])
        ans = 1
        arrowpos = points[0][1]
        
        for i in range(1, len(points)):
            if arrowpos >= points[i][0]:    #same arrow will work
                continue
            else:
                ans += 1
                arrowpos = points[i][1]
        return ans