class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #variable sliding window
        m = Counter(t)
        count = len(m)
        ans = math.inf
        
        i, j = 0, 0
        start, end = -1, -1
        
        while j < len(s):  
            if s[j] in m:
                m[s[j]] -= 1
                if m[s[j]] == 0:    count -= 1
            
            while count == 0:   #==k nhi kuki sare elements chaiye, 
                if ans > j-i+1:
                    ans = j-i+1
                    start, end = i, j
                    
                if s[i] in m:
                    m[s[i]] += 1
                    if m[s[i]] == 1:    count += 1
                i += 1
            j += 1
        
        return s[start:end+1]
         
    #feasble solutions are when count = 0. out of all feasible we need max window.
    

     