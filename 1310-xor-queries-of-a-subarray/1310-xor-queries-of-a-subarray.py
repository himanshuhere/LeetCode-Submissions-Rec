class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Before anything, **this problem and GFG Count Subarrays with Xor as K** ,  *This problem clears a lot of concepts*
        # Xor[0, i] ^ Xor [i, j] = Xor [0, j]
        # Xor[i, j] = Xor[0, j] ^ Xor[0, i] i-1 precisely
        d = {}
        res = []
        d[-1] = 0 #initialize it with -1 for first iter as it will be 0-1 = -1 so not error shud come na
        for i in range(len(arr)):
            d[i] = d[i - 1] ^ arr[i]
            
        for i, j in queries:
            res.append(d[i - 1] ^ d[j])
        return res