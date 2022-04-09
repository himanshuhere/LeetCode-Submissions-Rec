class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #you know quickselect?
        dic = Counter(nums)
        
        h = []
        for key, val in dic.items():
            heappush(h, (val, key))   
            if len(h) > k:
                heappop(h)
        
        
        return [key for _, key in h]   
        