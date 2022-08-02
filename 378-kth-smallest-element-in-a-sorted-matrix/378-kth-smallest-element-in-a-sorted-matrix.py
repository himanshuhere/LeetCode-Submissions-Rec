class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #Ready for interview
        #1 Sorting TC: MLOGM where M=n^n | SC: n^n
        #go throught entire matrix an dput then in a new array
        #sort array and find the kth index
        
        
        #2 maxheap | MlogK, M=n^n | logK
        def heap():
            maxheap = []
            for row in matrix:
                for c in row:
                    heappush(maxheap, -c)
                    if len(maxheap) > k:
                        heappop(maxheap)
            return -maxheap[0]
        
        
        #3 Binary search | Tc : nlogn | Space o(1)
        #not sorted for imaginary
        
        n, m = len(matrix), len(matrix[0])
        def countSmaller(num):
            i, j, cnt = 0, m-1, 0
            while i < n and j >= 0:
                if matrix[i][j] <= num:
                    cnt += (j+1)
                    i += 1
                else:
                    j -= 1
            return cnt
        
        def helper():
            lo, hi = matrix[0][0], matrix[-1][-1]
            while lo < hi:
                mid = lo + (hi-lo)//2
                if countSmaller(mid) < k:
                    lo = mid+1
                else:
                    hi = mid
            return lo
        
        return helper()