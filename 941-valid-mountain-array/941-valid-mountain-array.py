class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        #I can picture two persons climbing the mountain and trying to arrive at the same peak. Very straightforward and easy to understand.
        n = len(A)
        i, j = 0, len(A)-1
        while i + 1 < n and A[i] < A[i + 1]: i += 1
        while j > 0 and A[j - 1] > A[j]: j -= 1
        return 0 < i == j < n - 1