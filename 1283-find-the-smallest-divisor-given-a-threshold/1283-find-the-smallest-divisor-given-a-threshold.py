class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #n^2 brute force
        #okay yes you thought why not sum(arr) once and use same to devide by each number don win o(n)
        #yes would have its medium really you think thats easy, so it asked to take the ceil valuem and sum(arr) would be not equal if we take ciel for diff elememts, i mean len or sum or ciel etc they will change the sum for every element, so o(n) is there for every element. Now save other n, use BINARY SEARCH ON ANSWERS
        #answer - what? a devisor, whats the range? as per contraint 1 <= nums[i] <= 106
        #so min is  1, do we need 10^6 for max, mah because for every array max value is enought after that sum is always be smaller range = [1 - max(A)] lets do
        
        def blackBox(div):
            sm = 0
            for num in nums:
                # sm += ceil(num/div)
                sm += num//div          #if not use ceil
                if num%div != 0:
                    sm+=1
    
            return sm <= threshold
        
        
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = lo + (hi-lo)//2
            if(blackBox(mid)):
                hi = mid
            else:
                lo = mid + 1
        return lo