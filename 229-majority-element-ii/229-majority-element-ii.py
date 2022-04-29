class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #Boyer moore voting algo
        #There will be atmost two such elemets (zero, one or two)
        
        if not nums:
            return []
        
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:             #if elif elif jaruri hai verna can1, can2 bc ek ko hi pakd sakte h
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1     #teesra aaya to dono decremnt hoge
        
        #Now need to check, if both appears more than n/3
        count1, count2 = nums.count(candidate1), nums.count(candidate2)
                
        ans = []
        if count1 > len(nums)//3:       #that appear more than ⌊ n/3 ⌋ times.
            ans.append(candidate1)
        if count2 > len(nums)//3:
            ans.append(candidate2)
            
        return ans