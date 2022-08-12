class Solution:
    def candy(self, ratings: List[int]) -> int:
        #ye pura khud se kiya, ek round me fill kiya aur second round me kuch reh gye thik kiya unko ab dekhte h solution me kya kiya hai kese kiya hai
        #one more thing, earliar i thought DP kuki hard hai so try every possiblity but nhi related topic dekh liya wese nhi dekhna tha but sorry so greedy
        
        def selfdid():
            n = len(ratings)
            if n == 1:
                return 1
            if n == 2:
                if ratings[0] == ratings[1]:
                    return 2
                else:
                    return 3
            #1  
            coins = [1]*n
            coins[0] = (2 if ratings[0] > ratings[1] else 1)
            
            for i in range(1, n-1):
                if ratings[i] > ratings[i-1] and ratings[i] > ratings[i+1]:
                    coins[i] = max(coins[i-1], coins[i+1]) + 1
                elif ratings[i] > ratings[i-1]:
                    coins[i] = coins[i-1] + 1
                elif ratings[i] > ratings[i+1]:
                    coins[i] = coins[i+1] + 1

            coins[-1] = (coins[-2]+1 if ratings[-2] < ratings[-1] else coins[-1])

            
            #2
            coins[-1] = coins[-2]+1 if (ratings[-2]<ratings[-1] and coins[-1]<=coins[-2]) else coins[-1]
            for i in range(n-2, 0, -1):
                if ratings[i] > ratings[i-1] and ratings[i] > ratings[i+1]:
                    coins[i] = max(coins[i-1], coins[i+1]) + 1
                elif ratings[i] > ratings[i-1]:
                    coins[i] = coins[i-1] + 1
                elif ratings[i] > ratings[i+1]:
                    coins[i] = coins[i+1] + 1
            coins[0] = coins[1]+1 if (ratings[1]<ratings[0] and coins[0]<=coins[1]) else coins[0]        
            #print(coins)
            return sum(coins)
        
        def fromSolution():
            #Wow kinda same logic, but fucking clean.
            n = len(ratings)
            if n == 1:
                return 1

            # initial state: each kid gets one candy    
            nums = [1] * n
            
            #FOR interview, make separate list for boht direction and add max candy logic without MAX(), then again traverse over both list and extract max of same index. Then for optimization, remove one list and do on same list using max at second loop
            
            # kids on upwards curve get candies
            for i in range(1, n):
                if ratings[i] > ratings[i-1]:
                    nums[i] = nums[i-1] + 1

            # kids on downwards curve get candies, upward from back
            # if a kid on both up/down curves, i.e. a peak or a valley
            # kid gets the maximum candies among the two.
            for i in range(n-2, -1, -1):
                if ratings[i] > ratings[i+1]:
                    nums[i] = max(nums[i+1]+1, nums[i])

            return sum(nums)

        return fromSolution()
    
    
    #Do it in two directions.
# The first loop makes sure children with a higher rating get more candy than its left neighbor; the second loop makes sure children with a higher rating get more candy than its right neighbor.
