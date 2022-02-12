class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        #lil diff 
        n = len(arr)
        ans = 0
        i = 0
        while i < n:
            base = i
            while i < n-1 and arr[i] < arr[i+1]:
                i += 1
            if i == base:
                i += 1
                continue
            
            peak = i
            while i < n-1 and arr[i] > arr[i+1]:
                i += 1
            if i == peak:
                i += 1 
                continue
            
            mountain = i - base + 1
            ans = max(ans, mountain)
        return ans
                
            