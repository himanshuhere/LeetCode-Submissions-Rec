class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #seq vs subseq
        #see notes
        maxcount = 0
        nset = set(nums)        #set is must else TLE

        for num in nset:
            if num - 1 not in nset:
                currcount = 1
                while num + 1 in nset:
                    num += 1
                    currcount += 1
                maxcount = max(maxcount, currcount)
        return maxcount