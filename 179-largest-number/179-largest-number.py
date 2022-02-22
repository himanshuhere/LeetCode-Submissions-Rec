class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #Greedy
        #Best thing would be take two numbers, and decide which one should go first.
        #We ll use sort with compare dont worry, nlogn needs but
        #lets say 3, 30 then wll see 330 or 303, then decide that 3 needs first position.
        #Edge case, multiple 0s can be in string, only return 0
        
        #int -> str
        for i in range(len(nums)):
            nums[i] = str(nums[i])      #num can max be 100, no overflow. use str
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
            
        nums = sorted(nums, key=cmp_to_key(compare))
        
        ans = "".join(nums)
        
        #check if all zeros
        allzeroes = True
        for ch in ans:
            if ch != "0":
                allzeroes = False
                break
        
        return ans if not allzeroes else "0"
    
    
    ###########################################################################
    #def compare(n1, n2):
            # if n1 + n2 > n2 + n1:
            #     return -1
            # else:
            #     return 1
    #key=cmp_to_key() needs only [-1, 0, 1]. -1 if fist numbers is priority, 1 if second and 0 if both same.
    #since we dont need zero as if n1+n2 same from both side add aything so return 1 will work.
    #str(int(ans)) would work in python for zeroes, but other lang can have overflow. Careful!!
            