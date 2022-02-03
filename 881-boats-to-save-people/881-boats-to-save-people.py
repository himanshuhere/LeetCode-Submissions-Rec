class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #bhcnho kese mene adhe min me ek bar me bana diya solution
        #kabhi kabhi khud pe bharosa nhi hota
        #sorting+two pointer
        
        #atmost two people on boats, thus either l and r or only r
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
                
        #at last, l==r for odd people. weights of same person will get added and fark nhi pdta solution will not get affected as whatever answer will be one boat is going to go. so fine. else u can write one condition l==r, boats++