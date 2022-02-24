class Solution:
    def isHappy(self, num: int) -> bool:
        #happy number will get to 1 and keep going to 1 only. remember this will be useful
        #unhappy can get like 12 45 65 76 878 65 4 33 76, se it will be repeating at some number. se just need to check if repetition is happening at 1 or at other number like 76.
        #ofc it can be done using set, if same ele comes (non one) again unhappy
        #TC is hard to calculate can say for 1000 atmost op can be 1001.
        
        #CYCLE OKAY only one algo, slow and fast pointer. yes think like a linked list
        
        sl, fs = num, num
        while True:
            sl = self.sumSquares(sl)
            fs = self.sumSquares(self.sumSquares(fs))
            
            if sl == fs:            #either 1 or other number
                break
        return sl == 1
    
    def sumSquares(self, num):
        sq = 0
        while num:
            sq += (pow(num%10, 2))
            num //= 10
        return sq