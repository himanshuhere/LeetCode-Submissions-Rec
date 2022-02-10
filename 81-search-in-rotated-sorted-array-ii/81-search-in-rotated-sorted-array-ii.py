class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
                
            # the first half is ordered
            if nums[l] < nums[mid]:
                # target is in the first half
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            elif nums[l] > nums[mid]:
                # target is in the second half
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:                   #this is for eliminating duplicate else same as I. see find minimum in roated sorted array II
                l += 1
                
        return False