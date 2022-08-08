class Solution:
    def findLongestChain(self, nums: List[int]) -> int:
        #LIS
        #Prerequisite - LC #300 Plz
        nums.sort()
        n = len(nums)
        lis = [1]*n
        #cnt = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[j][1] < nums[i][0]:
                    if 1 + lis[j] > lis[i]:
                        lis[i] = lis[j] + 1
                    #     cnt[i] = cnt[j]                 #inherit
                    # elif 1 + lis[j] == lis[i]:
                    #     cnt[i] += cnt[j]                #increase the count
        mx = max(lis)
        # ans = 0
        # for i, n in enumerate(lis):
        #     if n == mx:
        #         ans += cnt[i]
        return mx