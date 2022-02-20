class Solution:
    def insert(self, A: List[List[int]], new: List[int]) -> List[List[int]]:
        #List is already sorted thus only o(N)
        #ask if not sorted, we can sort on start and apply our merge algo directly - nlogn
        i = 0
        ans=[]
        
        #skip the smaller parts than new[0]
        while i < len(A) and A[i][1] < new[0]:      #i.end < new.start : keep going
            ans.append(A[i])
            i += 1
            
        #keep merging till interval start smaller than new last
        while i < len(A) and new[1] >= A[i][0]:     #new.end >= i.start 
            new[0] = min(new[0], A[i][0])
            new[1] = max(new[1], A[i][1])
            i+=1
        ans.append(new)
        
        #add the rest part
        while i < len(A):
            ans.append(A[i])
            i+=1
        
        return ans
    
# If the given list was not sorted, we could have simply appended the new interval to it and used the merge() function from Merge Intervals. But since the given list is sorted, we should try to come up with a solution better than O(N * logN)

# When inserting a new interval in a sorted list, we need to first find the correct index where the new interval can be placed. In other words, we need to skip all the intervals which end before the start of the new interval. So we can iterate through the given sorted listed of intervals and skip all the intervals with the following condition: intervals[i].end < newInterval.start Once we have found the correct place, we can follow an approach similar to Merge Intervals to insert and/or merge the new interval. Let’s call the new interval a and the first interval with the above condition b. There are five possibilities:

# The diagram above clearly shows the merging approach. To handle all four merging scenarios, we need to do something like this:

#     c.start = min(a.start, b.start)
#     c.end = max(a.end, b.end)
# Our overall algorithm will look like this:

# Skip all intervals which end before the start of the new interval, i.e., skip all intervals with the following condition:
#     intervals[i].end < newInterval.start
# Let’s call the last interval b that does not satisfy the above condition. If b overlaps with the new interval (a) (i.e. b.start <= a.end), we need to merge them into a new interval c:
#     c.start = min(a.start, b.start)
#     c.end = max(a.end, b.end)
# We will repeat the above two steps to merge c with the next overlapping interval.