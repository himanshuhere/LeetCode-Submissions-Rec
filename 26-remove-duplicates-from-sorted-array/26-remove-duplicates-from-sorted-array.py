class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        #we gonna do it in same array
        
        #brute force is n logn for maintaing a set and puching ele and remove from them to array back
        #this is n , 1 with two pointer approach
        if len(A) == 0: return 0
        
    
        i, j = 0, 0
        
        while j < len(A):
            if A[i] == A[j]:
                j += 1
            else:
                i += 1
                A[i], A[j] = A[j], A[i]
                j += 1
        return i + 1