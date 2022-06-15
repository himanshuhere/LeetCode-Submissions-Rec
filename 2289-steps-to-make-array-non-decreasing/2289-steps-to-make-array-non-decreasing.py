class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        res,stack = 0, []
        for i in range(len(nums)-1,-1,-1):
            cur = 0
            while stack and nums[stack[-1][0]]<nums[i]:
                _,v = stack.pop()
                cur=max(cur+1,v)
            res = max(res,cur)
            stack.append([i,cur])
        return res
    
    
    #ulta traverse kyu, bcs you cant pop elemetns from stack if you proceed l to r, so in r to l. you can pop elements if s[-1] <num[i], and can count continous operation.
    #while popping you cant doing c+1, yes but lets say some elemtns comes which took more than c+1 steps we have to follow stick that chain right so take that instead
    
    
    
#     Consider the given testcase:
# [5,3,4,4,7,3,6,11,8,5,11]
# As per qns we can't delete the first element (In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.)
# so '5' is inevitable,
# now we have to remove elements less than 5 untill we meet other element right to '5' greater than '5'.
# we end up at '7' so far we delete "3" nums.
# untill '11' we delete "2" nums.
# untill next '11' we delete "2" nums.
# so answer would be max deletions taken place Therefore, ans=3
# ********************* BUT WAIT ******************
# if we consider :
# [14,1,2,3,4,5,6,1,2,3,4]
# we would get ans=10(Which is WRONG!!!)
# Because,
# we could delete nums 1 2 3 4 5 6 wrt '14' and other 1 2 3 4 nums wrt '6'
# Then answer would be 6 actually.
# SO WHAT TO DO !!!
# lets see,
# if we iterate the array from end which is right to left.
# now lets do the same but in other way
# lets take a stack contains elements of form [nums[i],deletions_it_can_do]
# so when we iterate it from right we find 4 we append [4,0] to stack
# next we find '3' which is smaller than '4' we continue
# ...
# we'll reach '6' there are 4 nums right to it so we append [6,4]
# each time ans would be max(ans,stack[i][1])
# simillarly we reach '14' we append [14,5]
# so ans=5!!
# (With this we predict the deletions we should make at max as we would have done 10 before wrt 14 but now we know that 6 helps us with few(4) parallel deletions so ans=5.)
# (See code explanation below for complete explanation.)

# CODE:

# class Solution:
#     def totalSteps(self, nums: List[int]) -> int:
#         ans = 0
#         nums.reverse()
#         lst = [[nums[0], 0]]
#         for i in range(1, len(nums)):
#             cnt = 0
#             while lst and lst[-1][0] < nums[i]:
#                 cnt = max(cnt + 1, lst[-1][1])
#                 print(lst)
#                 lst.pop()
#             lst.append([nums[i], cnt])
#             ans = max(ans, cnt)
#         return ans