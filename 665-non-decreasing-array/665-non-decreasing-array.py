class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = False
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                if flag:
                    return False
                if (i-2>=0 and i+1<n and nums[i-1]>nums[i+1] and nums[i-2]>nums[i]):
                    return False
                flag = True
        return True