class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        #pascal triangle only
        if poured == 0:
            return 0
        
        pre = [poured]
        while query_row:
            tmp = []
            tmp.append(max((pre[0]-1)/2, 0))
            for i in range(1, len(pre)):
                tmp.append(max((pre[i-1]-1)/2, 0) + max((pre[i]-1)/2, 0))
            #tmp.append(max((pre[-1]-1)/2, 0))
            tmp.append(tmp[0])
            query_row-=1
            
            pre = tmp
            
        return min(pre[query_glass], 1)
        
        

        

#                              n
#                      (n-1)/2  (n-1)/2
# ((n-1)/2-1)/2  ((n-1)/2-1)/2+((n-1)/2-1)/2  ((n-1)/2-1)/2
# so onn..

#n
#(n-1)/2  (n-1)/2
#((n-1)/2-1)/2  ((n-1)/2-1)/2+((n-1)/2-1)/2  ((n-1)/2-1)/2
# so onn..
