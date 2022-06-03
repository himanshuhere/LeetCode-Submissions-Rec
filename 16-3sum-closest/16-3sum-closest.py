class Solution:
    def threeSumClosest(self, A: List[int], target: int) -> int:
        #skipping duplicates will boost performance

        res = A[0] + A[1] + A[2]
        A = sorted(A)
        for i in range(len(A)-2):
            if i == 0 or i > 0 and A[i-1] != A[i]:  #can remove this too
                l, r = i+1, len(A)-1

                while l < r:
                    cursum = A[i]+A[l]+A[r]
                    if cursum > target:
                        r-=1
                    else:
                        l+=1

                    if abs(res-target) > abs(cursum-target):
                        res = cursum
        return res
        