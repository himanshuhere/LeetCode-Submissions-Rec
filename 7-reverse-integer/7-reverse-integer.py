class Solution:
    def reverse(self, x: int) -> int:
        #kuch nhi last se nikalo new me lagate jao dekh lo ek bar, neg bas alag se handle karna
        
        neg = False
        if x < 0:
            neg = True
            x = -x
            
        new = 0
        while x:
            last = x%10
            x //= 10
            new = new*10+last
        
        if neg:
            new = -new
        if not (-2**31<=new<=2**31-1):
                return 0
        return new
        