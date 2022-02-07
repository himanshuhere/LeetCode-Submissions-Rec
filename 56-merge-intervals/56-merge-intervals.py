class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)   #first key toh sorted, for second key we keep max element see
        ans = []
        i = 0
        j = -1
        while i < len(intervals)-1:
            
            if intervals[i][1] >= intervals[i+1][0]:
                j = i
                seckey = intervals[i][1]        #ye nhi kroge to error bahot ayege casec me
                while j < len(intervals)-1 and seckey >= intervals[j+1][0]:
                    j += 1
                    seckey = max(seckey, intervals[j][1])
                    
                ans.append([intervals[i][0], seckey])
                i = j + 1
                
            else:
                ans.append([intervals[i][0], intervals[i][1]])
                i += 1
        
        if j < len(intervals)-1:
            ans.append(intervals[-1])
            
        return ans