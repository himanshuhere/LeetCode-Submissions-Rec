class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        #greatest to the right using stack
        right = [0]*len(temp)
        st = []
        for i in range(len(temp)-1, -1, -1):
            while st and temp[st[-1]] <= temp[i]:        #
                st.pop()
            if st:
                right[i] = st[-1] - i
            else:
                right[i] = 0
            
            st.append(i)
            
        return right
    
    
        res = [0] * len(T)
        stack = []
        
        for index in range(len(T)-1, -1, -1):
            
            while stack and T[stack[-1]] <= T[index]:
                stack.pop()
                        
            res[index] = stack[-1] - index if stack else 0
            
            stack.append(index)

            
        return res