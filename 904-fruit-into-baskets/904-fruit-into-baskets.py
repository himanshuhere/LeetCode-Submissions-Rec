class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #read and understand, its sliding window variable window size problem
        #arra or string, find longest window/subarray/substring with 2 unique char
        if len(fruits) == 1: return 1
        
        i = j = ans = 0
        d = defaultdict(int)
        
        while j < len(fruits):
            d[fruits[j]] += 1
            
            if len(d) <= 2:
                ans = max(ans, j - i + 1)
                j += 1
            else:
                while len(d) > 2 and i < j:
                    d[fruits[i]] -= 1
                    if d[fruits[i]] == 0:
                        d.pop(fruits[i])
                    i += 1
                j += 1
        return ans