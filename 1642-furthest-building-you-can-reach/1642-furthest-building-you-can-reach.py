class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        n = len(h)
        #min-heap
        #keep going, add jumps to ladder till len of heap is equal to ladders so ladders is sorted cool, now whatever jump after comes heap will sort and give min jump so use bricks for that, once bricks ends that the point u need to stop as u already have ladders indices in heaps.
        #when i tried first tracing jumps and putting in heap, and then again second iteration tried doing this things, i was not geeting ans as possibly there might be biggest jumps in the heap and that is in last index say, so once bricks ends how come we decide to iuse the ladders from last etc.
        
        h_ = []
        for i in range(n-1):
            if h[i] < h[i+1]:
                heappush(h_, h[i+1]-h[i])
                if len(h_) > l:
                    b -= heappop(h_) 
                    if b < 0:
                        return i
        return len(h)-1
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         @lru_cache(None)
#         def helper(i,j,k): # i indexes heights, j is bricks, k is ladders
#             if i == n - 1:
#                 return n-1
#             else:
#                 if h[i+1] <= h[i]: 
#                     return helper(i+1,j,k)
#                 else:
#                     maxIndex = i
#                     if j >= h[i+1]-h[i]:
#                         maxIndex = max(maxIndex,helper(i+1,j-(h[i+1]-h[i]),k))# use bricks
#                     if k > 0:
#                         maxIndex = max(maxIndex,helper(i+1,j,k-1)) # use ladders
#                     return maxIndex
        
#         return helper(0,b,l)
        