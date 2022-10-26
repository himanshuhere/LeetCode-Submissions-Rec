class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m = defaultdict(int)
        m[0] = -1
        r = 0
        s = 0
        while r < len(nums):
            s += nums[r]
            if s%k in m:
                if r-m[s%k] > 1:
                    return True
            else:
                m[s%k] = r
            r += 1
        return False
                
        