class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        #Tried DP, you will get the result but TLE why becasue you are taking k jumps everytime just to get the max of that range. Can we optimize this, maybe heap - logn or maybe decreasing queue, where everytume front you get maximum val. o(1), i mean heap is better but this is more better. atleast you ll understand a new way to optimize heap op. n-logn-1.
        #thats it other than this everything is dp only tabulation yes.
        #top down - k^n, tabulation - n*k, dp+queuue = n
        #but then you ll always pop rear values from queue, everytime you will get front as max, (is it in range)
        #yes you also need to make sure that queue is in range of k.
        
            n = len(nums)
            dp = [None]*n
            dp[n-1] = nums[n-1]
            q = deque([n-1])
            
            for i in range(n-2, -1, -1):
                dp[i] = nums[i] + dp[q[0]]
                
                while q and dp[q[-1]] <= dp[i]: #monotonic q to dp pe hi operate hoga pura
                    q.pop()
                q.append(i)
                
                if q[0] - i >= k: 
                    q.popleft()
                    
            return dp[0]
        
        
# Intuition:
# For any position, there are k ways to jump to that position. we have to choose maximum value from this k ways and add that value into current position.

# Let say, ith position has ways from i-k to i-1 as window.

# for example i=5, k =3, so the ways are start from (5-3) to (5-1) that is 2,3,4. We have to choose maximum value from this ways or window.

# Lets consider the following example

# nums = [10,-5,-2,4,0,3], k = 3
# we are looping each element,
# At each position,

# We are picking maximum value from previous choices.
# Add that maximum value into curr element and update in nums array.
# Add updated curr value in the queue.
# We start from 0th index, it does not have previous elements, we are adding current element in the queue.
# queue = []

# At index 1 has one choice. So maximum at this position is 10 and curr element is -5 (10-5) =5.
# queue = [10]

# At index 2 has two choices, so maximum is 10 and curr element is -2 (10-2)=8;
# queue = [10,5]

# At index 3 has three choices, maximum is 10 and curr is 4 (10+4)=14.
# // in Dequeue, to maintain the max element, we removing smallest element from queue.
# // in below queue, 8 is maximum than 5, so we are removing 5 from the queue.
# queue = [10,5,8] ->queue = [10,8]

# // when insert 14, 14 is maximum than 8,10. so we are removing them
# queue = [10,8] ->queue = [14]

# At index 4, the max is 14 and curr is 0, 14+0 = 14
# queue = [14]

# At index 5, the max is 14 and curr is 3, So 14+3=17
# queue = [14]

# finally return the last element as a result.