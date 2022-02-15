class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        #very easy o(4n)
        n = len(nums)
        mn = 2 ** 31
        mx = -2 ** 31
            
        for i in range(n-1):
            if nums[i] > nums[i + 1]:
                mn = min(mn, nums[i + 1])

        for i in range(n-1, 0, -1):
            if nums[i - 1] > nums[i]:
                mx = max(mx, nums[i - 1])


        l = 0
        for i in range(n):
            if mn < nums[i]:
                l = i
                break

        r = 0
        for i in range(n-1, -1, -1):
            if mx > nums[i]:
                r = i
                break

        return r - l + 1 if r > l else 0

      