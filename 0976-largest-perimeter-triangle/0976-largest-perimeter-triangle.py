class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # math - a<=b<=c, a+b>c for triagle to be valid
        A = sorted(nums)                #A = sorted(nums)[::-1]
        for i in range(len(A) - 3, -1, -1):
            if A[i + 2] < A[i + 1] + A[i]:
                return A[i + 2] + A[i + 1] + A[i]
        return 0