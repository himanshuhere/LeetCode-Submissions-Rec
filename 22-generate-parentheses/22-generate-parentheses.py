class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #aditya, backtracking
        res = []
        
        def fun(op, cl, temp):
            if op == cl == 0:
                res.append(temp)
                return
            
            if op:
                fun(op-1, cl, temp + "(")
            
            if cl > op:
                fun(op, cl-1, temp + ")")
            
        fun(n, n, "")
        return res