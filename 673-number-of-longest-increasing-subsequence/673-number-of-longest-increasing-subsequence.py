class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        #Prerequisite - LC #300 Plz
        n = len(nums)
        lis = [1]*n
        cnt = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if 1 + lis[j] > lis[i]:
                        lis[i] = lis[j] + 1
                        cnt[i] = cnt[j]
                    elif 1 + lis[j] == lis[i]:
                        cnt[i] += cnt[j]
        mx = max(lis)
        ans = 0
        for i, n in enumerate(lis):
            if n == mx:
                ans += cnt[i]
        return ans