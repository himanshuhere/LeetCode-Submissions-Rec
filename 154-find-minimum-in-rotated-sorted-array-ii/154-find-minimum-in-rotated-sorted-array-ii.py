class Solution:
    def findMin(self, A: List[int]) -> int:
        #UNIQUE ELEMENTS and sorted rotated, only < and > case no ==
#         lo, hi = 0, len(A) - 1
#         while lo < hi:
#             mid = lo + (hi - lo) // 2
            
#             if A[mid] < A[hi]:        #means, this plus elements on left can be ans, so take this too
#                 hi = mid
                
#             else:     #A[mid]>A[hi],means defintly smallers values is on right side better than this so leave this too
#                 lo = mid + 1
#         return A[lo]
                
        
        #DUPLICATES ELEMENTS and sorted rotated - why it is an issue and a hard ques in LC, because see you condition is based on > or < o eliminating left or right space. if mid and high are equyal how would you make decision where smaller lies, i mean in between those could as this is sorted. Since we are dealing with mid and high, we ll do one more thing for == case high--, if mid and low then lo++. this will not let us lose the ans since mid will always held this. see Worst case - o(n)
        
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if A[mid] < A[hi]:        #means, this plus elements on left can be ans, so take this too
                hi = mid
                
            elif A[mid] > A[hi]:      
                lo = mid + 1
            
            else:   #=== case
                hi -= 1
                
        return A[lo]
                
        