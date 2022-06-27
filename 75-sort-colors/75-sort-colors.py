class Solution:
    def sortColors(self, a: List[int]) -> None:
        l = m = 0
        r = len(a)-1
        while m <= r:
            if a[m] == 0:
                a[m], a[l] = a[l], a[m]
                l += 1
                m += 1
            elif a[m] == 2:
                a[m], a[r] = a[r], a[m]
                r -= 1
            else:
                m += 1
        
    
    
    
    #see notes
    #1 - sort - nlog | 2 - count 0,1,2 and modify - n | 3 - dutch national flag - n three pointer
        
#         i, j = 0, len(nums)-1
#         mid = 0
        
#         #beg to mid = 0, mid to end = 1, else after end = 2
        
#         while mid <= j:         #since while loop has only mid, j, they need to move 
#             if nums[mid] == 0:
#                 nums[mid], nums[i] = nums[i], nums[mid]
#                 i += 1
#                 mid += 1
#             elif nums[mid] == 2:
#                 nums[mid], nums[j] = nums[j], nums[mid]
#                 j -= 1              #dont inc mid, might possible 2,2 hi swap huye or 0 agya ho mid me end se usko i se swap bhi karna hai isliye let mid be there
#             else:
#                 mid += 1
                
#         #see left se mid i sath chale the to sure hai 0s hi hai udhar but right se 0 ya 2 ay 1 kuch b swap ho sakta hai to let mid be there and check once again