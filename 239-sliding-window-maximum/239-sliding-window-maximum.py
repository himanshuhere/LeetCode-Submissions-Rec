class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Aditya fixed sliding window format, and use of deque or maybe stack to maintain maximums for windows see
        q = deque()
        ans = []
        i, j = 0, 0
        
        while j < len(nums):
            
            #remove all the smaller value present in q, no use now since we have bigger
            while q and q[-1] < nums[j]:
                q.pop()
            #now push the bigger one
            q.append(nums[j])
            
            if (j-i+1) == k:
                ans.append(q[0])
                if q[0] == nums[i]:
                    q.popleft()
                i += 1
            j += 1
        
        return ans