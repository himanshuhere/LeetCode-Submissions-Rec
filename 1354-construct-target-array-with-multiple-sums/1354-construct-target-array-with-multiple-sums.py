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
        