class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        #bahut simple hai hit nhi horaha tha. see sorted hai to logn me chaiye
        #see One imp thing, A[index] - (index + 1) tells how many missing numbers are there before current index
        #1 5 7 8, say i = 3, A[i] = 8, => A[i] - i+1 ==> 8-3+1==>4, 4 number missing there 
        #thats true see,  2 3 4 6 are missing. we ll use same logic see
        
        lo, hi = 0, len(arr)-1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if arr[mid] - (mid+1) < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo + k       #missing number