class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
    
    
        currsum = sum(nums)
        actsum = len(nums) * (len(nums) + 1) // 2
        return actsum - currsum
    
    
    #or can apply cyclic sort algo
        i = 0
        while i < len(nums):
            if nums[i] == nums[nums[i]]:    #else swap wud have handled ths i know but it is imp to ignore inf loop in program
                i += 1
            else:
                nums[i], nums[nums[i]] = nums[nums[i]], nums[i]

        for i in range(len(nums)):
            if nums[i] != i:
                return i

            
    #The time complexity of the above algorithm is O(n). In the while loop, although we are not incrementing the index i when swapping the numbers, this will result in more than n iterations of the loop, but in the worst-case scenario, the while loop will swap a total of n-1 numbers and once a number is at its correct index, we will move on to the next number by incrementing i. In the end, we iterate the input array again to find the first number missing from its index, so overall, our algorithm will take O(n) + O(n-1) + O(n) which is asymptotically equivalent to O(n).