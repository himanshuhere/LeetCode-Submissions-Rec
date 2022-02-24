class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #read and understand, its sliding window variable window size problem
        #arra or string, find longest window/subarray/substring with 2 unique char
        if len(fruits) == 1: return 1
        
        i = j = ans = 0
        d = defaultdict(int)
        count = 0
        
        while j < len(fruits):
            d[fruits[j]] += 1
            if d[fruits[j]] == 1:
                count += 1
            
            #i<j not needed here, but for other ques like this while sometimes i crosses j and create neative reult and keep in mind
            while count > 2 and i < j:      
                d[fruits[i]] -= 1
                if d[fruits[i]] == 0:
                    count -= 1
                i += 1
            
            ans = max(ans, j - i + 1)
                
            j += 1
        return ans