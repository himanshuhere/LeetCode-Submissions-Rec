class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        #overlapped part b/w two intervals can be calculated as
#         start = max(a.start, b.start)
#         end = min(a.end, b.end) 
#         That is, the highest start time and the lowest end time will be the overlapping interval.

#         So our algorithm will be to iterate through both the lists together to see if any two intervals overlap. If two intervals overlap, we will insert the overlapped part into a result list and move on to the next interval which is finishing early.
        
        
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            #check if first interval has overlapping with seccond
            first = A[i][0] >= B[j][0] and A[i][0] <= B[j][1]
            
            #check if second has any intersection with first
            second = B[j][0] >= A[i][0] and B[j][0] <= A[i][1]
            
            if (first or second):
                ans.append( [ max(A[i][0], B[j][0]), min(A[i][1], B[j][1]) ] )  #only take the intersection part
    
            #move next from the interval which is finishing first
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans