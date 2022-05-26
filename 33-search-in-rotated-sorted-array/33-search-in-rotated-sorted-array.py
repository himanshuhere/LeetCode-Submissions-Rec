class Solution:
    def search(self, A: List[int], target: int) -> int:
        #see notes solution i thought and easy to understand yet long to see
        n = len(A)
        if n == 0: return -1

        
        #why basic template of lo <= hi and mid-1 and mid+1, because its a search BS algo, we find at mid we return bcs we have target to search, ques like min max upper bound lower etc arent exact target so we focus on eliminating and returning lo, keep in mind direct search where you write if A[mid] == target: return mid, will based on basic template only.
        #same if duplicates, make if else < and > then else lo+=1 if dealing with lo and mid else hi -= 1, to discard duplicates
        
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if A[mid] == target: return mid     #imp for this search algo
            
            # inflection point to the right. Left is strictly sorted
            if A[lo] <= A[mid]:
                if A[lo] <= target <= A[mid]: #if in left
                    hi = mid - 1
                else:
                    lo = mid + 1      #if in right
                    
            # inflection point to the left of me. Right is strictly increasing
            else:
                if A[mid] <= target <= A[hi]:    #if in right
                    lo = mid + 1
                else:
                    hi = mid - 1         #if in left
            
        return -1
    
    
    
    
    
    
#     while low < high:
#         mid = (low+high)//2
#         if ar[low] < ar[mid]:
#             if ar[low] <= tar <= ar[mid]:
#                 high = mid
#             else:
#                 low = mid + 1
#         else:
#             if ar[mid] < tar <= ar[high]:
#                 low = mid + 1
#             else:
#                 high = mid
    