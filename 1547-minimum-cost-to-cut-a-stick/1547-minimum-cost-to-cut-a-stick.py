class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        #MCM - PARTITION DP
        #cuts can be in any order but if wanna go DP recursing you have to have cuts in sorted way else left right calls of i..j will be messed up. second imp thing is that every time we make cut we take the lenght of current stick in account and thats something to take care of since you ll be given on cuts location in array but stick is something diff like 3,4,7,8 is actually 1,2,3,4,5,6,7,8,9 or anything. so inorder to calc lenght we have something see, we are appeneding the actual cuts ( both ends ) and can use them, recusrsivey we ll always have i-1, j+1 as left and right cuts and can have lenght of curr rod
        
        cuts = [0] + cuts + [n]
        cuts.sort()
        
        @lru_cache(None)
        def f(i, j):
            if i > j:
                return 0
            
            mini = math.inf
            for k in range(i, j+1):
                cost = cuts[j+1] - cuts[i-1] + f(i, k-1) + f(k+1, j)
                mini = min(mini, cost)
            return mini
        
        print(cuts)
        return f(1, len(cuts)-2)