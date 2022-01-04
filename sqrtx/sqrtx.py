class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):    #bcz integer part value we need so close reuslt wud consider
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1
        return 0
    