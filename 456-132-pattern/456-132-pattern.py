class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #I GUESS Monotonic inc stack banana hai but mere ko ek kam k liye ek loop aata h lets see pehle wo, then ek monotonic inccreasing array banayege kuki small number chaiye and ek me hi dono end ka kam ho jayega
#         left, right = [-1]*len(nums), [-1]*len(nums)
#         st = []
#         #nsl
#         for i in range(len(nums)):
#             while st and nums[st[-1]] > nums[i]:
#                 st.pop()
#             left[i] = nums[st[-1]] if st else nums[i]-1
#             st.append(i)
            
#         st = []
#         #nsr 
#         for i in range(len(nums)-1, -1, -1):
#             while st and nums[st[-1]] > nums[i]:
#                 st.pop()
#             right[i] = nums[st[-1]] if st else nums[i]-1
#             st.append(i)
#         for i in range(len(nums)):
#             if left[i] < right[i] < nums[i]:
#                 print(i)
#                 return True
#         return False
    
    #NOPES, didnt work for all test cases, issue is with the ele whose left or right is not possible. i have tried none, max, min nothing worked. That thoda socha solution dekhu to pata chala dimag ka prayog karna hai mene kaha ohh isliye merese nh bana. 
    #Baat esi hai 132, means left me 1 and 1 is smallest of 132. So just create a min prefix array so from any index you can get the minimest ele possible, since 2 is greater than 1 but smallet than 3, so on right side we cant go for the minimal (that worked on left as 132), so for right NSR but for left prefix array . Now while going we ll keep checking if curr nums[i] is > than min[i] then only operate on stack and find the right bigger, once found(after all popping) see the condition met or not if yes return true else revise. See code
    
        min_list = list(accumulate(nums, min))
        stack, n = [], len(nums)
        
        #NSR
        for j in range(n-1, -1, -1):
            if nums[j] > min_list[j]:           #is 3 > 1 / nums[i] > min[i] holds then only look for 2
                
                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:       #this should min[i](left)1 < stack[-1](right)3 < nums[i](curr)3
                    return True
                stack.append(nums[j])  
                
        return False
    
        