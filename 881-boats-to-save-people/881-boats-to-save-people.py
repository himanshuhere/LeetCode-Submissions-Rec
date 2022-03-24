class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #Two pointer 
        
        A = sorted(people)
        ans = 0
        i, j = 0, len(A)-1
        while i <= j:
            if A[i]+A[j] > limit:
                if A[i]>A[j]:
                    i += 1
                else:
                    j -= 1
            else:
                i += 1
                j -= 1
                
            ans += 1
        return ans