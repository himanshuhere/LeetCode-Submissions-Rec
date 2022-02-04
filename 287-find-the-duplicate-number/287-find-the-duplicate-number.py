class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n = len(nums)-1
        # return abs( (n*(n+1))//2 - sum(nums)) nah dint work for more than 2 duplicates
        
        #came up with diff approach of marking see if works hope
        #o(n)
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:           #negative/marked/visited
                return abs(nums[i])                   #duplicate
                
            else:
                nums[abs(nums[i])] = -nums[abs(nums[i])]  #mark it
                
                #ye abs ne bahot dimag khaya
        
        
        #there is one more official one, but since we have done it in o(n) by our own algo yes cool, so better keep this in mind its cool also
        #baki dekh lo
        #How can we prove that at least one duplicate number must exist in nums?

        
        #Floyd's Tortoise and Hare (Cycle Detection)
        slow = fast = nums[0]
        while True:                 #do while cuz abhi to same pos me hai break ho jayega loop
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break
            
        fast = nums[0]
        while slow != fast:         #isme nhi hoga
            slow = nums[slow]
            fast = nums[fast]
        return slow
