class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # sliding window + double ended queue
        #put index
        mx, mn = collections.deque([0]), collections.deque([0])
        ans = 1
        i = 0
        
        for j in range(1, len(nums)):
            # update max and min monotonic q
            while mx and nums[mx[-1]] < nums[j]:
                mx.pop()
            mx.append(j)
            while mn and nums[mn[-1]] > nums[j]:
                mn.pop()
            mn.append(j)
            
            while mx and mn and nums[mx[0]] - nums[mn[0]] > limit:
                i += 1
                if mx[0] < i:
                    mx.popleft()
                if mn[0] < i:
                    mn.popleft()
                    
            ans = max(ans, j-i+1)
            
        return ans