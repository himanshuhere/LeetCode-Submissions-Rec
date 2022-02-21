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
  #getEarliest = minHeap()
    
# Here is what our strategy will look like:

# We will sort the meetings based on start time.
# We will schedule the first meeting (let’s call it m1) in one room (let’s call it r1).
# If the next meeting m2 is not overlapping with m1, we can safely schedule it in the same room r1.
# If the next meeting m3 is overlapping with m2 we can’t use r1, so we will schedule it in another room (let’s call it r2).
# Now if the next meeting m4 is overlapping with m3, we need to see if the room r1 has become free. For this, we need to keep track of the end time of the meeting happening in it. If the end time of m2 is before the start time of m4, we can use that room r1, otherwise, we need to schedule m4 in another room r3.
# We can conclude that we need to keep track of the ending time of all the meetings currently happening so that when we try to schedule a new meeting, we can see what meetings have already ended. We need to put this information in a data structure that can easily give us the smallest ending time. A Min Heap would fit our requirements best.

# So our algorithm will look like this:

# Sort all the meetings on their start time.
# Create a min-heap to store all the active meetings. This min-heap will also be used to find the active meeting with the smallest end time.
# Iterate through all the meetings one by one to add them in the min-heap. Let’s say we are trying to schedule the meeting m1.
# Since the min-heap contains all the active meetings, so before scheduling m1 we can remove all meetings from the heap that have ended before m1, i.e., remove all meetings from the heap that have an end time smaller than or equal to the start time of m1.
# Now add m1 to the heap.
# The heap will always have all the overlapping meetings, so we will need rooms for all of them. Keep a counter to remember the maximum size of the heap at any time which will be the minimum number of rooms needed.
# function minMeetingRooms(meetings) {
#   //JavaScript does not come with built in Heap, so I used an array to keep track of rooms and sorted by end time at each call
#   if(meetings == null) return 0
#   if(meetings.length <= 1) return meetings.length
  
#   //helper that returns the meeting room with the earliest end time
#   function getEarliest(room) {
#     room.sort((a,b) => a[1]-b[1])
#     return rooms[0]
#   }



#CODE
#   //sort meetings on start time
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
# }