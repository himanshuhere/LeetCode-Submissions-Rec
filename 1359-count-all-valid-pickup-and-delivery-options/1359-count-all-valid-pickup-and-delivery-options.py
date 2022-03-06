class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        
    #maths one
    #for pickup we can put anywhere so n! ways but for deliveries we have like 1.3.5.7... from last delivery to first. so total summations of 2n-1
    #for n=1, we have 1*(2n-1) then (n-1)*(2n-3), 
    #n*(2n-1), (n-1)*(2n-3), (n-2)*(2n-5) , .............  
        
        res = 1
        for i in range(1, n+1): #pickeups
            res = res*i
            res %= MOD
            
        for i in range(1, n+1): #deliveries
            res = res*(2*i-1)
            res %=MOD
            
        return res
        
        #Top down
        #since pickeup has no constraints and first pickup and then deli is possible for N we have 2N spaces. so we ll pick one and go for delivery or pick three and go for delivery like open close brancket we have qes in backtrackng. Might be case then after one picku two deliveries gonne made, so wll take take with [to_deliver_yet > picked] to make a call for delivery.
        #ways 
        @lru_cache(None)
        def f(unpicked, undel):
            if unpicked == 0 and undel == 0:
                return 1
            if unpicked < 0 or undel < 0 or undel < unpicked:
                return 0
            
            ans = 0
            #if unpicked > 0:
            ans += unpicked*f(unpicked-1, undel)
            ans %= MOD
            
            #if undel > unpicked:
            ans += (undel - unpicked)*f(unpicked, undel-1)
            ans %= MOD
            
            return ans
    
        return f(n, n)
        
#see why unp*f(unp-1, und), beacuse see as only for pick. Like permutation for first place we have n ways and then n-1 ans so on like if n = 4 then only for pickup since we dont have any constraints we have 4.3.2.1 = 4! ways. thus
#for deliveries, we have only the number of ways which already has picked, thus (undel-unpicked)=this is like 1 is picked so from 4 we have 4-(unpicked) that is 4-3 thus 1 delivery to made, lil confusing but still.
#And yes factorial ways will not work for deliveries as they depends on pickup placing thus we pick first then made call to delivery and looking for all kind of possiblities and return 0 for unwanted.
#For for clarified ans see math one third solution down


        #Tab
        dp = [[0] * (n + 1) for i in range(n + 1)]
        dp[0][0] = 1
        for unpicked in range(n + 1):
            for undelivered in range(1, n + 1): #(i, n + 1) this is more good
                if unpicked > 0:
                    dp[unpicked][undelivered] += unpicked * dp[unpicked - 1][undelivered]
                dp[unpicked][undelivered] %= MOD
                
                if undelivered > unpicked:
                    dp[unpicked][undelivered] += (undelivered - unpicked) * dp[unpicked][undelivered - 1]
                dp[unpicked][undelivered] %= MOD
        
        return dp[n][n]
    
    
    
    