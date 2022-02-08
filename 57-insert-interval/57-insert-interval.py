class Solution:
    def insert(self, A: List[List[int]], new: List[int]) -> List[List[int]]:
        i = 0
        ans=[]
        
        #skip the smaller parts than new[0]
        
        while i < len(A) and A[i][1] < new[0]:
            ans.append(A[i])
            i += 1
            
        #keep merging till interval start smaller than new last
        if i < len(A):
            minn = min(new[0], A[i][0])         #as sorted, these two are only participants here
            new[0] = minn
        while i < len(A) and A[i][0] <= new[1]:
            new[1] = max(new[1], A[i][1])
            i+=1
        ans.append(new)
        
        #add the rest part
        while i < len(A):
            ans.append(A[i])
            i+=1
        
        
        return ans
    
#or second step
        # while i < len(A) and A[i][0] <= new[1]:
        #     new[0] = min(new[0], A[i][0])
        #     new[1] = max(new[1], A[i][1])
        #     i+=1
        # ans.append(new)