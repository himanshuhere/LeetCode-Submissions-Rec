#Stack - Nearest greatest to the left - NRL

#This is brute force, working right without stock. okay TLE for last 10 test cases
# class StockSpanner:

#     def __init__(self):
#         self.arr = []

#     def next(self, price: int) -> int:
#         n = self.arr
#         if not self.arr:
#             self.arr.append(price)
#             return 1
        
#         self.arr.append(price)
#         psudo_index = 0
#         for i in range(len(n)-2, -1, -1):
#             if self.arr[i] > price:
#                 return len(n)-i-1
#         return len(n) - psudo_index 
 
#using stack and dimag dusro ka
class StockSpanner:

    def __init__(self):
        self.s = []     #pair (price, span)     #span = elements smaller including this to left

    def next(self, price: int) -> int:
        span = 1            #curren count
        while self.s and self.s[-1][0] <= price:
            span += self.s[-1][1]
            self.s.pop()     #becasue if price is greater, right values will stop at price only, and span will help to get the totol count
        
        self.s.append((price, span))
        return span
        
 

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)