class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # A row of asteroids is stable if no further collisions will occur. After adding a new asteroid to the right, some more collisions may happen before it becomes stable again, and all of those collisions (if they happen) must occur right to left. This is the perfect situation for using a stack.
        #was lil tough as did visualize stack as vertical rather horizontal. Better for array problem start thinkiung like horizontal stack proccesing either to left or right.
        #this problem idea is same like balance paranthesis,( , ) => -ve, +ve 


        st = []
        for num in asteroids:
            flag = "push"
            
            while st and num < 0 and st[-1] > 0:
                diff = num + st[-1]
                
                if diff < 0:            #num is bigger
                    st.pop()
                elif diff > 0:          #stack has top value bigger let it be and dont push
                    num = 0                 #use num only, flag has scope issues, num can be 0 as given cant be 0
                else:
                    st.pop()
                    num = 0
                    
            if num:
                st.append(num)
                
        return st