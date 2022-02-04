class Solution:
    def getMinSwaps(self, nstr: str, k: int) -> int:
        def nextPermutation(nums):
            ind1 = len(nums)-2
        
            #1 - find smaller ele from right
            while ind1 >= 0 and nums[ind1] >= nums[ind1+1]:
                ind1 -= 1
            
            if ind1 == -1:               #nums are in descending order, edge case
                return nums.reverse()

            #2 fing bigger first element that ind1
            ind2 = len(nums)-1                
            while nums[ind2] <= nums[ind1]:
                ind2 -= 1

            #swap them
            nums[ind1], nums[ind2] = nums[ind2], nums[ind1] 

            #reverse the numbers after ind1
            l, r = ind1+1, len(nums)-1  # reverse the second part
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1 ; r -= 1
                
            return nums
        
        def get_swap_count(nums, nums0) -> int:
            count = 0
            for i in range(len(nums)):
                if nums[i] != nums0[i]:
                    
                    index = i + 1
                    while nums0[index] != nums[i]:
                        index += 1

                    # print(i, index)
                    while index != i:
                        nums0[index], nums0[index-1] = nums0[index-1], nums0[index]
                        #print("after swap: ", ("").join(nums0))
                        count += 1
                        index -= 1
            return count
        
        
        new = list(nstr)
        for _ in range(k):
            new = nextPermutation(new)
        return get_swap_count(list(nstr), list(new))