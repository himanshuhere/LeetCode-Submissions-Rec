class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #bhcnho kese mene adhe min me ek bar me bana diya solution
        #kabhi kabhi khud pe bharosa nhi hota
        #sorting+two pointer
        
        A = sorted(people)
        l, r = 0, len(A)-1
        boats = 0 
        while l <= r:
            weights = A[l]+A[r]
            if weights > limit:
                r -= 1                  #bcs surely r is max than l, greedly fill boat with r
            else:
                l += 1
                r -= 1
                
            boats += 1
        return boats
                