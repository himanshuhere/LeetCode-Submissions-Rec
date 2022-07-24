class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # see notes
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1      # for n * n, n will work but there are test with m * n thus this
        
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            if target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False
        
    # you can not apply imaginary binary search here cuz as a list it is not sorted
    # this is more suitable for 74 problem
#         if not matrix or not matrix[0]:
#             return False

#         l, r = 0, len(matrix)*len(matrix[0])

#         while l<r:
#             mid = (l+r)//2
#             i, j = mid//len(matrix[0]), mid%len(matrix[0])
#             if matrix[i][j]==target:
#                 return True
#             elif matrix[i][j]>target:
#                 r = mid
#             else:
#                 l = mid + 1
    
#         return False