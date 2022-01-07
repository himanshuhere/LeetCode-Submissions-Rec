class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo = 0
        hi = len(arr) - k
        #pls read notes pls
        
        while lo < hi:
            mid = lo + (hi - lo)//2     #consider mid as start of our ans range 1-k
			
            if x <= arr[mid]:
                hi = mid
            elif x >= arr[mid + k]:
                lo = mid + 1
                
            elif arr[mid] < x < arr[mid + k]:
                if x - arr[mid] > arr[mid + k] - x: #which is close side
                    lo = mid + 1
                else:
                    hi = mid
                
        return arr[lo : hi + k]
    
    
    #2 - soemthing wrong in logic
        
#         myheap = [[]]
        
#         for i in arr:
#             heapq.heappush(myheap, [abs(i - x), i])
#             if len(myheap) > len(arr) - k:
#                 ans.append(heapq.heappop(myheap)[1]
        
#         ans = []
#         for i in myheap:
#             ans.append(i[1])
        
#         return ans