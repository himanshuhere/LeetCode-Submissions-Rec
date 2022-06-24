class Solution:
    def isPossible(self, A: List[int]) -> bool:
        total = sum(A)
        A = [-a for a in A]
        heapq.heapify(A)
        
        while True:
            m = -heapq.heappop(A)
            total -= m
            if m == 1 or total == 1: 
                return True
            if m < total or total == 0 or m % total == 0:
                return False
            m %= total                      #instead m-=total 
            total += m
            heapq.heappush(A, -m)
            
            
        
        #% accelerate kar rha kaam like [100, 3] -> [97, 3] -> [94, 3] agar apni tarike se kiya jo hai m -== total, but while lopp 33 bar chalega and will make [1, 3], but if using % while loop ek bar chalega bas. So multiple subs converted into quotent and we dont care about quotient here, only reminder better use %
        