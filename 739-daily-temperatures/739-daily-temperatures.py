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
    
    
    