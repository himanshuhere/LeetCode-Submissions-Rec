class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, ts: int) -> int:
        #contest - biweekly | 5 feb - 2022
        # if ts == 6008:
        #     return 65817
        
        arr = []
        
        m, s = str(ts//60), str(ts%60)
        if int(m) <= 99 and int(s)<=99:
            if len(m) == 1: m = "0"+m
            if len(s) == 1: s = "0"+s
            arr+=[m+s]
        
        
        m1, s1 = str(int(m)-1), str(int(s)+60)
        if int(m1) <= 99 and int(s1)<=99:
            if len(m1) == 1: m1 = "0"+m1
            if len(s1) == 1: s1 = "0"+s1
            arr.append(m1+s1)
        
        def getCost():
            st = str(startAt)
            i = 0
            cost=0
            patt= str(int(arr[k]))
            
            while i < len(patt):
            
                if st == patt[i]:
                    #print("push")
                    cost += pushCost
                    i+=1
                else:
                    #print("move")
                    
                    cost+=moveCost
                    st = patt[i]
            return cost
        
        ans = math.inf
        for k in range(len(arr)):
            ans = min(ans, getCost())
        return ans 
            
        
        
        
        
            