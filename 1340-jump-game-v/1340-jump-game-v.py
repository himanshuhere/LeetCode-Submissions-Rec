class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        
        @lru_cache(None)
        def dfs(i):
            x = 0
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[i] <= arr[j]:    #ek b bada hai range me break not possible aage
                    break
                x = max(x, dfs(j))
                
            for j in range(i - 1, max(0, i - d) -1, -1):
                if arr[i] <= arr[j]: 
                    break 
                x = max(x, dfs(j))
            return 1 + x
        
        return max(dfs(i) for i in range(n))
#pehle mai check kar raha tha if arr[i] > arr[j] then go but nhi ek b bada mile break wahi se
