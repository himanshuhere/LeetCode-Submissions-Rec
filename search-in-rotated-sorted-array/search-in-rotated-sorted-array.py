class Solution:
    def search(self, A: List[int], target: int) -> int:
        #see notes solution i thought and easy to understand yet long to see
        n = len(A)
        left, right = 0, n - 1
        if n == 0: return -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == target: return mid
            
            # inflection point to the right. Left is strictly increasing
            if A[mid] >= A[left]:
                if A[left] <= target <= A[mid]: #if in left
                    right = mid - 1
                else:
                    left = mid + 1      #if in right
                    
            # inflection point to the left of me. Right is strictly increasing
            else:
                if A[mid] <= target <= A[right]:    #if in right
                    left = mid + 1
                else:
                    right = mid - 1         #if in left
            
        return -1