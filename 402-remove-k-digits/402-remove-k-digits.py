class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #Actual MONOTONIC STACK
        
        #Brute pls code like your brain thinks, your brain will pick out first lets say k=1
        # 1432219
        # remove every ele once and you ll get = (432219, 132219, 142219, 143219, 143219, 143229, 143221)
        # which is smaller = 132219(4 erased) now for this also
        # 132219 = (32219, 12219, 13219, 13219, 13229, 13221) - samller 12219 (erase 3 not 9)
        #means everytime you remove first peak, first i such that a[i] > a[i+1]
        def brute():
            while k:

                i = 0
                while i < len(num)-1 and num[i] <= num[i+1]:    #<= imp
                    i += 1
                #num.pop(i)
                num = num[:i] + num[i+1:]

                k -= 1

            #trim
            #i = 0
            # while i < len(num) and num[i] == '0':
            #     num = num[1:]
            #     i += 1
            num = num.lstrip("0")       #strip, lstrip, rtrip
            return num if num != "" else "0"    #
    
    #STACK see we need to remove first dip we get, and keep removing with k--, we also need to keep doing it for k only. 
        st = []
        
        for i in range(len(num)):
            while k and (st and st[-1] > num[i]):
                st.pop()
                k -= 1
            
            #for leading zero, leading can only be when stack is empty and zero comes
            if not st and num[i] == "0":    continue
            st.append(num[i])
        
        #for case like 1234, 1111, nothing will pop and k will still be there, so remove last elements
        while k and st:
            st.pop()
            k -= 1
        
        if not st:  
            return "0"
        return "".join(st)
        
    
    
    
    
    
    
    
        