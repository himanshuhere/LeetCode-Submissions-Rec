class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        aplh = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        ans = ''
        
        #-1 karna jaruri hai else %26 har bar 26 ya uske multiplier ko 0 kar dega aur hum kabhi Z print hi nhi karege else har bar A, okay i tried putting Z at 0th index also but that will ruin rest characters indexing. thus better make 1th based indexing of column to 0th everytime as it gets reset by //26
        while columnNumber:
            columnNumber -= 1
            ans += aplh[columnNumber%26]
            columnNumber = (columnNumber)//26
        
        return ans[::-1]
    
    
    # It is like converting a decimal number to base26 except there is no zero in that we need to subtract 1 from n to make that adjustment to get the answer we get from convert a normal decimal number to any base.
# Time: O(k) - k is the numer of digits in the input
# Space: O(1)

        res = ""
        n = columnNumber
        while n:
            n = n-1                 # to make the offset cuz 0 isnt considering here in base26excel
            c = chr(n%26 + ord('A'))     # ord to get ascii else error
            res += c
            n = n//26
        return res[::-1]
    
    # res = c + res and return direct res