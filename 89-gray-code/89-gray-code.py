class Solution:
    def grayCode(self, n: int) -> List[int]:
        #peep code dekhna ya notes
        res_bin = []
        res_bin = self.genGrayCode(n)
        res_int = []
        for binary in res_bin:
            res_int.append(int(binary, 2))
        
        return res_int

    def genGrayCode(self, A):
        if A == 1:
            return ["0", "1"]
        
        temp = self.genGrayCode(A-1)
        res = []
        for i in range(len(temp)):
            res.append(str(temp[i])+"0")

        for i in range(len(temp)-1, -1, -1):
            res.append(str(temp[i])+"1")
        
        return res