class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        #lil diff 
        n = len(arr)
        ans = 0
        i = 0
        while i < n:
            base = i
            while i < n-1 and arr[i] < arr[i+1]:    #keep climbing
                i += 1
            if i == base:                           #dint climb, still at base only come again at i+1
                i += 1
                continue
            
            peak = i
            while i < n-1 and arr[i] > arr[i+1]:    #keep sliding down
                i += 1
            if i == peak:                           #couldnt come, still at peak?
                i += 1 
                continue
            
            mountain = i - base + 1                 #take the current trek distance
            ans = max(ans, mountain)
        return ans
                
            