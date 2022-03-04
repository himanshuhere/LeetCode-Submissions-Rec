class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        #arr = [[0]*101 for _ in range(101)]
        arr = [[0]*(query_glass+2) for _ in range(query_row+1)]
        
        arr[0][0] = poured
        for i in range(query_row):      #one level less is fine, we already calcuting next row
            for j in range(query_glass+1):  #but col we need to reach
                rem = max(arr[i][j] - 1, 0) 
                arr[i+1][j] += rem/2
                arr[i+1][j+1] += rem/2
        ans = arr[query_row][query_glass] 
        return ans if ans <= 1 else 1