class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        len_ = len(costs)
        ans = 0
        diff = [0]*len_
        for i in range(len_):
            ans += costs[i][0]
            diff[i] = costs[i][1] - costs[i][0]
        
        diff.sort()
        
        for i in range(len_//2):
            ans += diff[i]
            
        if len_%2 != 0:
            if diff[len_//2+1] <= 0:
                ans += diff[len_//2+1]
                
        return(ans)