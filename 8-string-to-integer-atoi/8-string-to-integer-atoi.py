class Solution:
    def myAtoi(self, s: str) -> int:
        #see notes
        str = s.strip()
        if len(str) == 0:
            return 0
        
        ans = "0"   #in case +/- nhi hua to 0 rahega to int value me issue nhi karega ye result = int(tmp)
        result = 0
        
        i = 0
        if str[0] in "+-":  
            ans = str[0]    #0 ya + ya -
            i += 1
        
        for i in range(i, len(str)):
            if str[i].isdigit():
                ans += str[i]
            else:           #if char non - digit
                break       #loop hi chor dene ka pehla ele letter ku na ho bhaiya hmko khelna hi nhi h
                
        if len(ans) > 1:    #else bhai nhi aya kuch kayki ek length to rehni hi hai + ya - ya 0
            result = int(ans)
            
        
        MAX_INT = 2 ** 31 - 1   #inclusion
        MIN_INT = -2 ** 31
        
        if result > MAX_INT:
            return MAX_INT
        elif result < MIN_INT:
            return MIN_INT
        else:
            return result
        