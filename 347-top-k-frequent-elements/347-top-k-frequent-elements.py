import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dic = Counter(nums)
        
        max_heap = []
        for key, val in dic.items():
            heappush(max_heap, (val, key))   
            if len(max_heap) > k:
                heappop(max_heap)
        
        
        return [key for _, key in max_heap]   
        

        