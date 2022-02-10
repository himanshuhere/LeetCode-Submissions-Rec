class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #sliding window can be used variable one but for only positives number, here negatives also there sliding window will not work. but map can be but HOW. think of s[i,j] = s[0,j]-s[0,i], now see will put every sum frim left to right in map if again found will increase count. Since we just need to return count of  window subarryas with sum k, not max windows not min, window can of any size just sum should be k. so whenevr we found that cur sum - k, already present then we found ans, but could be possible that sum-k can also be occured multiple times back then thus we have count in map, take entire count and add that to final res.
        
        map_ = defaultdict(int)
        res = 0
        sum_ = 0
        map_[0] = 1     #dont know why this works but this worked--means sum 0 is 1 there, if you doint take any presum means subarray from 0th iundex to here at i
        for num in nums:
            sum_ += num
            if sum_ - k in map_:
                res += map_[sum_ - k]
            
            #fill map
            map_[sum_] += 1
        return res
    
    #nlogn