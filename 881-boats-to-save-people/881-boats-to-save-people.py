class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        A = sorted(people)
        l, r = 0, len(A)-1
        boats=0
        while l<=r:
            weights = A[l]+A[r]
            if weights <= limit:
                l+=1
                r-=1
            else:
                r-=1
            boats+=1
        return boats
                