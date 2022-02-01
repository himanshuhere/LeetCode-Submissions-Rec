class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        sm = 0
        i, j = 0, 0
        ans = 0
        while j < len(arr):
            sm += arr[j]
            
            if j-i+1 == k:
                if sm//(j-i+1) >= threshold:
                    ans += 1
                sm -= arr[i]
                i += 1
            j+=1
        return ans