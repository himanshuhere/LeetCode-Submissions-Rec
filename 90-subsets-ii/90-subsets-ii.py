class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def sub2(i, tmp):
            ans.append(tmp[:])
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:  continue
                tmp.append(nums[j])
                sub2(j+1, tmp)
                tmp.pop()
        
        
        def sub(i, tmp, preChosen):
            if i == n:
                ans.append(tmp[:])
                return
            
            #no take
            sub(i+1, tmp, False)
            
            #take
            if i > 0 and not preChosen and nums[i] == nums[i-1]:  return 
            
            tmp.append(nums[i])
            sub(i+1, tmp, True)
            tmp.pop()
            
            # // If the previous number is same as current number i.e., if nums[i - 1] == nums[i], 
            # // and if previous number was chosen(i.e., choosePre is true),
            # // then dont re-include the current number because it would then be a duplicate
            
            
            
        
        nums.sort()
        ans = []
        #sub(0, [], False)
        sub2(0, [])
        return ans