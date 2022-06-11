class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        rep = defaultdict(int)
        ans = 0
        for n in nums:
            if n in rep:
                ans += rep[n]
            rep[n] += 1
        return ans