class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #sorted hota to two pointer lo hi, unique hai to repetetion handle nhi karne, map and o(n) loop
        #brute
        n = len(nums)
        for i in range(n):
            comp = target - nums[i]
            for j in range(i + 1, n):
                if comp == nums[j]:
                    return [i, j]
        return []
    
        #see notes
        h = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp not in h:
                h[num] = i
            else:
                return [h[comp],i]