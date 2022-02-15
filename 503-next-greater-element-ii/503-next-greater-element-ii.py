class Solution:
    def nextGreaterElements(self, A: List[int]) -> List[int]:
        #NGR
        #trick, loop twice the array
        #NGR
        #we will follow same NGR logic, only since asked for circular list searching
        #thus take an imaginary double list and modify for range and i % n
        
        n = len(A)
        ngr = [0] * n
        stack = []
        
        for i in range(2*n - 1, -1, -1):
            while stack and A[stack[-1]] <= A[i % n]:
                stack.pop()
            ngr[i % n] = A[stack[-1]] if stack else -1
            stack.append(i % n)
        
        return ngr
                
        
        #n^2 sol me do loop honge i and j, j will start from i+1 right, okay now see jabhi b do loop me second loop j is dependent upon i for looping tabhi optimiaze karne k liye stack laga sakte ho socho hmesah n solution banega ofc with spaceres = []
        
    
    #also sometime we need to play with indces in stack, pls take care that too
        #and this is also ngr, instead right to left do left to right, and pop and assig do inside whole only
        stack, res = [], [-1] * len(A)
        
        for i in range(len(A)*2):
            while stack and (A[stack[-1]] < A[i%len(A)]):
                res[stack.pop()] = A[i%len(A)]
            stack.append(i%len(A))
        return res