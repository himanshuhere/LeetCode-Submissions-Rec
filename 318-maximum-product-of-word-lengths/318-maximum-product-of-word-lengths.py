class Solution:
    def maxProduct(self, w: List[str]) -> int:
        # def f(s1, s2):        #this is wrong bcs n^2
        #     for i in s1:
        #         if i in s2:
        #             return False
        #     return True
        
        
        #convert words to int so comparing can be done in o(1)
        #how - bit is 32, we need 26 each letter is 1 then present in word simple, how to on that bit use OR and why 1 << (), so a-a cant be 0, we need a = 1, so one shift thats all.
        
        mask = [0]*len(w)
        for i, word in enumerate(w):
            for c in word:  
                mask[i] |= 1 << (ord(c) - ord('a'))        #on the cth bit
        
        ans = 0
        for i in range(len(w)):
            for j in range(i+1, len(w)):
                if mask[i] & mask[j] == 0:
                    ans = max(ans, len(w[i])*len(w[j]))
        return ans