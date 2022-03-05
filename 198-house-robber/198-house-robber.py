class Solution:
    def rob(self, A: List[int]) -> int:
        #alternate robbing doesnt pass all test cases - same ques with tree also there there will start from root
        #at every step we can skip any number houses this makes it DP
        @lru_cache(None)
        def fn(i):
            #if house ends, no money 0
            if i < 0:
                return 0
             
            return max(A[i]+fn(i-2), 0+fn(i-1))
            #either robb current house money and skip one then decide further
            #dont robb this house and go to next and further
            #chose the max money robbed
            
        
        return fn(len(A)-1)