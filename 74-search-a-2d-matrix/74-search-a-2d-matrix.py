class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #dekho yaha pe row wise sorted hai to yaha imag binary search lagao better TC else other ques me row col dono sorted hai but row wise nhi to bin search nhi lag sakti better ye algo lagao top right cell 
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
        
        
        
    # second approach imaginary binary search most optimal
        if not matrix or not matrix[0]:
            return False

        l, r = 0, len(matrix)*len(matrix[0])

        while l<r:
            mid = (l+r)//2
            i, j = mid//len(matrix[0]), mid%len(matrix[0])
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                r = mid
            else:
                l = mid + 1
    
        return False
	