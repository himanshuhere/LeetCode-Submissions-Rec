class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #o(log(n-k))
        lo = 0
        hi = len(arr) - k
        
        #pls read notes pls
        #mid = leftmost ele of our solution range 1 to k
        while lo < hi:
            mid = lo + (hi - lo)//2     #consider mid as start of our ans range 1-k
			
            if x - arr[mid] > arr[mid+k] - x:
                lo = mid + 1
            else:
                hi = mid
                
        return arr[lo : lo + k]
    
    
    #2 - soemthing wrong in logic - heap is also brute sol
        
#         h = []
        
#         for i in arr:
#             heapq.heappush(h, (-abs(i - x), i))
#             if len(h) > k:
#                 heapq.heappop(h)
#         ans = []
#         for x,y in h:
#             ans.append(y)
        
#         return ans