class Solution:
    def arrangeCoins(self, n: int) -> int:
        # #1 Linear
        # row = 1
        # while n >= row:
        #     n -= row
        #     row += 1
        # return row-1
        
        #2 Binary Search 
        # range is sorted 1-n
        # 1 + 2 + 3 + 4 ... k = k*(k+1)/2, thus for kth row we need that formula coins
        
        lo, hi = 1, n
        ans = 0
        while lo <= hi:
            row = (lo+hi) >> 1
            coinsneed = row*(row+1)//2
            
            if coinsneed <= n:
                ans = row
                lo = row + 1
            else:
                hi = row - 1
        return ans
            
        