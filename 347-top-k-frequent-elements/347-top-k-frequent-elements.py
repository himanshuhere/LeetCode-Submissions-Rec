class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = []
        for ele in c:
            heappush(h, (c[ele], ele))
            if len(h) > k:
                heappop(h)
        return [ele for freq, ele in h]