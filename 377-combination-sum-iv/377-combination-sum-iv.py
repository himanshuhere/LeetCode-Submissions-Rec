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
        
        return f(0, target)
        