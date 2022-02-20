class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     Sort the intervals on the start time to ensure a.start <= b.start
    # If a overlaps b (i.e. b.start <= a.end), we need to merge them into a new interval c such that:
    # c.start = a.start
    # c.end = max(a.end, b.end)
    #since sorted on first key, we need to check only second now. do test case graphical
        n = len(intervals)
        ans = []
        
        intervals = sorted(intervals)       #sort on first key
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] <= end:      #overlapping
                end = max(end, intervals[i][1])
            else:                           #no overlap, add previous st,end and update wth current
                ans.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        #add the last one
        ans.append([start, end])
        return ans
                
    