class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n =len(A)
        i=0
        j=n-1
        res=[]
        
        while i <= j:
            if A[i]*A[i] >= A[j]*A[j]:
                res.append(A[i]*A[i])
                i += 1
            else:
              res.append(A[j]*A[j])
              j -= 1
        
        return res[::-1]