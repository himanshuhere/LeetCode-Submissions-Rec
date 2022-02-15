class Solution:
    def nextGreaterElements(self, A: List[int]) -> List[int]:
        #NGR
        #trick, loop twice the array
        #and this is also ngr, instead right to left do left to right, and pop and assig do inside whole only
        stack, res = [], [-1] * len(A)
        
        for i in range(len(A)*2):
            while stack and (A[stack[-1]] < A[i%len(A)]):
                res[stack.pop()] = A[i%len(A)]
            stack.append(i%len(A))
        return res