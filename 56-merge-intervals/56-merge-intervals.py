class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     Sort the intervals on the start time to ensure a.start <= b.start
    # If a overlaps b (i.e. b.start <= a.end), we need to merge them into a new interval c such that:
    # c.start = a.start
    # c.end = max(a.end, b.end)
    #since sorted on first key, we need to check only second now. do test case graphical - o(nlogn)
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
                
        
        #lets say if only ask to check if overlap present. Do same but return True after if condition
    
    
    
    #1 Meeting rooms - need to check how many meeting one can attend
    #sort on start and then
#     //sort intervals by start time
#       appointmentTimes.sort((a,b) => a[0] -b[0])

#       //check if any two intervals overlap
#       for(let i = 1; i < appointmentTimes.length; i++) {
#         if(appointmentTimes[i][0] < appointmentTimes[i-1][1]) {
#           //note that in the comparison above, it is < and not <=
#           //while merging we needed <= comparison, as we will be merging the two 
#           //intervals have conditions appointmentTimes[i][0] === appointmentTimes[i-1][1]
#           //but such intervals don't represent conflicting appointments
#           //as one starts right after the other
#           return false
#         }
#       }
#       return true


#meeting - 2
#use min heap for ending time
#rooms will have number of rooms currently having meetings, just like real world implementation see
# //sort meetings on start time
#   meetings.sort((a,b) => a[0]-b[0])
  
#   let rooms = [meetings[0]]
  
#   for(let i = 1; i < meetings.length; i++) {
#     let earliestRoom = getEarliest(rooms)
#     let currentTime = meetings[i]
    
#     //if the room time ends before the currentTime interval starts
#     //then use the room and update the room end time to currentTime
#     if(earliestRoom[1] <= currentTime[0]) {
#       earliestRoom[1] = currentTime[1]
#     } else {
#       //create room
#       rooms.push(currentTime)
#     }
#   }
#   return rooms.length