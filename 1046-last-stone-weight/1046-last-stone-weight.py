class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # first, negate all weight values in-place
        for i, s in enumerate(stones):
            stones[i] = -s
        heapify(stones)  # pass all negated values into the min-heap
        
        while stones:
            s1 = -heappop(stones)  # the heaviest stone
            if not stones:  # s1 is the remaining stone
                return s1
            s2 = -heappop(stones)  # the second-heaviest stone; s2 <= s1
            if s1 > s2:
                heappush(stones, -(s1-s2))  # push the NEGATED value 
            # else s1 == s2; both stones are destroyed
        return 0  # if no more stones remain