class Solution:
    def grayCode(self, n: int) -> List[int]:
        #peep code dekhna ya notes
        a = self.genGrayCode(n)
        for i, num in enumerate(a):
            a[i] = int(num, 2)
        return a

    def genGrayCode(self, A):
        if A == 1:
            return ["0", "1"]
        
        temp = self.genGrayCode(A-1)
        cur = []
        for i in range(len(temp)):
            cur.append("0" + str(temp[i]))

        for i in range(len(temp)-1, -1, -1):
            cur.append("1" + str(temp[i]))
        
        return cur