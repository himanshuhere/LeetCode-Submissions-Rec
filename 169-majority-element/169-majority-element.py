class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #there are many solutions, sort, hashmap, but looking for boyer moore voting algorith
        
        # nums.sort()
        # return nums[len(nums)//2]     n/2 elements will be filled with half list
        
        # Boyer-Moore Voting Algorithm -  worth to understacd, guaranteed algo
        mcandidate = None       # or -1
        count = 0
        
        for num in nums:
            if count == 0:
                mcandidate = num
                
            if num == mcandidate: 
                count += 1
            else: 
                count -= 1
                
        return mcandidate
        #if count of mcandidate not >= n/2 means it is not maj cadidate and then there is no maj candidate here since algo is guranteed 
    