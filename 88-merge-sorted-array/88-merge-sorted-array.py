class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
         #without extra space
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
                
        if n > 0:
            nums1[:n] = nums2[:n]
            #In the case where the while loop terminates and nums2 still contains numbers, we know those numbers are the lowest numbers.
#We still need to add those numbers.
