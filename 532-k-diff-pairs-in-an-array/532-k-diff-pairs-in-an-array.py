class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:     
        ans = 0
        s = Counter(nums)
        if k == 0:
            for i in s:
                if s[i] > 1:
                    ans += 1
        else:         
            for num in s:
                if num+k in s:
                    ans+=1
        return ans