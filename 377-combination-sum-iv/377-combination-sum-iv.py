class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #Initially i did take not take, but see waha pe you go forward only and here any order combination is possible
        #okay so i thought of doing same on nums then nums[::-1], but how would you eliminate duplicates okay plus there are many other issues
        #then i thought if we can chose any element after any, lets loop over entire array, means select one and then again go 0-n, then select any and again go to 0-n, but gives Recursion maximum limit exceeded, because then not take function case was not necessary, yes its a loop it handles not take case through loop itself.
        
        @lru_cache(None)
        def f(i, t):
            if t==0:
                return 1
            if t < 0 or i == len(nums):
                return 0
            ans = 0
            for j in range(len(nums)):
                ans += f(j, t-nums[j])
            return ans
        
        #return f(0, target)
        
        #2
        @lru_cache(None)    #dp use memo if not this else TLE
        def f(tar):
            if tar == 0:
                return 1
            if tar < 0:     #iski jagah loop k andar call se pehle >=0 cond b aa sakti
                return 0
            
            comb = 0
            for j in range(0, len(nums)):
                comb += f(tar-nums[j])
            return comb
        
        return f(target)
        
        
        #3
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        
        for i in range(1, target + 1):
            for j in nums:
                if i - j >= 0:
                    dp[i] += dp[i - j]
                    
        #return dp[target]