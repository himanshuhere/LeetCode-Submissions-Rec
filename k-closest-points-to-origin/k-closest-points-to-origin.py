class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #HEAP se socho katai easy lagega dimag me
        #x1, x2 from origin 0, 0 is under root of x1^2 + x2^2
        # we ll store (key, pair) in heap so key wud be distance as heap will sort on first arg key
        #one more thing, if every ans is going to be under root so ignore under root calc just see x1^2 + x2^2
        
        myheap = []
        heapify(myheap)
        
        #max heap banana hai isliye - lagaya dist me
        for x,y in points:
            dist = x*x + y*y
            heappush(myheap, (-dist, [x,y])) #heap sort on base of first ele pushed here freq
            if len(myheap) > k:
                heappop(myheap)
        
        return [ points for d, points in myheap]