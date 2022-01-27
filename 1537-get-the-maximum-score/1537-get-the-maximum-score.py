class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        sum1, sum2 = 0, 0
        res = 0
        i, j = 0, 0
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:                       #checkpoint
                res += max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
                sum1, sum2 = 0, 0
            
        while i < m:
            sum1 += nums1[i]
            i += 1
        while j < n:
            sum2 += nums2[j]
            j += 1
        
        res += max(sum1, sum2)
        return res % int(1e9+7)
            
            
#         Logic is simple:
#             Let's say that a place where nums1[i] = nums2[j] is checkpoint.
#             Then result will be max prefix sum of two arrays + checkpoint + max sum postfix of two arrays
#             Or: max(sum(nums1[0:i]), sum(nums2[0:j]) + checkpoint + max(sum(nums1[i + 1:]), sum(nums2[j + 1:]))

#             So what we need to do is:

#             Iterate through two arrays with calculating sum until we find checkpoint
#             Add larger sum to result.
#             Add checkpoint to result.
#             Reset sums.
#             Repeat.
# Imagine we are not calculating sum1 and sum2 on evry turn instead we gonna use max(sum(nums1[0:i]), sum(nums2[0:j]), then how we will increment i and j. Ofc if nums1[i] is smaller then there might be chance that next value is a checkpoint as both are sorted array. So use this knowledge and sum1 and sum2 is better doing on loop to save time.
        
        