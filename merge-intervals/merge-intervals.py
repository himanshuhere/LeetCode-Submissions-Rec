class Solution:
    
    
    #1
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        A.sort()
        ans, i = [], 0
        while i < len(A):
            k = A[i][1]
            j = i
            while j < len(A)-1 and k >= A[j+1][0]:
                j += 1
                k = max(k, A[j][1])
            ans.append([ A[i][0], k ])
            i = j
            i+=1
        return ans
    
    #2 -solved after exploring discussion. Its smooth.
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        A = sorted(A)
        i = 0
        ans=[]
        ans.append(A[0])
        
        for i in range(1, len(A)):
            if ans[-1][1] >= A[i][0]:
                ans[-1][1] = max(ans[-1][1], A[i][1])
            else:
                ans.append(A[i])
        return ans
                    