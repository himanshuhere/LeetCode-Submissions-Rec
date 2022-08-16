class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #HEAP se socho katai easy lagega dimag me
        #x1, x2 from origin 0, 0 is under root of x1^2 + x2^2
        # we ll store (key, pair) in heap so key wud be distance as heap will sort on first arg key
        #one more thing, if every ans is going to be under root so ignore under root calc just see x1^2 + x2^2
        
#         myheap = []
#         #heapify(myheap)
        
#         #max heap banana hai isliye - lagaya dist me
#         for x,y in points:
#             dist = x*x + y*y
#             heappush(myheap, (-dist, [x,y])) #heap sort on base of first ele pushed here freq
#             if len(myheap) > k:
#                 heappop(myheap)
        
#         return [points for d, points in myheap]


        def partition_(l, r):
            pi = random.randint(l, r)
            nums[pi], nums[r] = nums[r], nums[pi]   #r is pivot now, so using r, pivot = nums[r]
            
            i = l
            pivot = nums[r][0]*nums[r][0]+nums[r][1]*nums[r][1]
            for j in range(l, r):
                f = nums[j][0]*nums[j][0]+nums[j][1]*nums[j][1]                
                if f <= pivot:                                      #<= rakhna jaruri h tabhi chala
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        
        def quickselect(l, r, k):
            if l >= r:
                return nums[:l]
            
            pi = partition_(l, r)        #pi is actually no of elements on left
            
            if pi == k:
                return nums[:pi]
            elif pi < k:
                return quickselect(pi+1, r, k)
            else:
                return quickselect(l, pi-1, k)

        
        nums = points
        n = len(nums)
        return quickselect(0, len(nums)-1, k)
            
            