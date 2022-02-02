class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #BINARY SEARCH ON ANSWERS. How d you figured it out actually i dint. was takig striver masterclass and he did this ques. but for sure one hack i found or say observation or pattter. No for binary search on answer, but for this feasible or black box function what you call. See allocate books also asked "MAXIMIZE THE MINIMUM values somehtins" OR "MINIMIZE THE MAXI..", here also it asked to minimize the max sum of diff m subarrays. actually ques ko samjhna bahot imp h to understand this, but kahi b lage that it is max the min or min the max, pls thing of a valid answer range and if that is fine then apply BS ona answers.
        #One more thing i learned, that range of answer also depends on contraints, see here if n subarray asked, then max subarray sum is the max(ele) and if 1 subarray is asked sum(arr) is the max one. so range is [max(arr) - sum(arr)]
        #No intuitive to me now, dont worry will come soon. Some things here too, range always lies or most of the times, like 0 , 1, min, max, sum, yes think and try every possibility. Cant confirm in things but hope patterns will hint me. now code
        #TC = O(nLog(sum-max))
        
        def feasible(threshold) -> bool:
            subs = 1
            sm = 0
            for num in nums:
                sm += num
                if sm > threshold:
                    sm = num
                    subs += 1
                    if subs > m:
                        return False
            return True

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                hi = mid     
            else:
                lo = mid + 1
        return lo