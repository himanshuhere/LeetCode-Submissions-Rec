class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        diff = math.inf
        
        for num in nums:
            if num % 2 == 0:
                heappush(heap, -num)
            else:
                heappush(heap, -num*2)
        
        _min = -max(heap)

        while True:
            _max = -heappop(heap)
            diff = min(diff, _max-_min)
            
            if _max % 2 == 1:               #got odd
                break

            heappush(heap, -_max//2)
            _min = min(_min, _max//2)

        return diff
        
        
            
        
        #no dp sad ;( 
        #Algo
#         note : even can be devide multiple times till it make odd
#                odd can be one multiply to make even
#         1. make all odds even by multipying them, put then in space (even as given)
#         2. now, take out the min, value.
#         3. now take the max, do max-min, capture the deviation and to reduce it devide the max value and put it in space. (max value we took was definately eve thus devide, now that can be odd or even)
#         3. lets say even, now again capture max-min, this time more smaller good.
#         4 again do same. But kab tak, till max value gets odd. thats when you cant reduce number(only even can, odd gets multiply) But min value can be operate know no? no bcs while tjhis operation going on we ll also check if max after division gets min that actual min, so now this is new min.
#         5. IMP, thing this was not the same max, max gets changes evertime, we take the max from space.
#         6. Space - max heap (make sense?)
#         7. operate on any element test case.

        
        
        