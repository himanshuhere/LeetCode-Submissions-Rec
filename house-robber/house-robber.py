class Solution:
    def rob(self, A: List[int]) -> int:
        #alternate robbing doesnt pass all test cases - same ques with tree also there there will start from root
        #at every step we can skip any number houses this makes it DP
        @lru_cache(None)
        def fn(i):
            #if house ends, no money 0
            if i > len(A)-1:
                return 0
                        
            #either robb current house money and skip one then decide further
            ans1 = A[i]
            ans1 += fn(i+2)
            
            #dont robb this house and go to next and further
            ans2 = 0
            ans2 += fn(i+1)
            
            #chose the max money robbed
            return max(ans1, ans2)
        
        return fn(0)