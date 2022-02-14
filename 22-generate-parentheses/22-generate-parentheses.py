class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #aditya, backtracking
        res = []
        open = close = n
        
        def fun(open, close, temp):
            if open == close == 0:
                res.append(temp)
                return
            
            if open:
                fun(open-1, close, temp + "(")
            
            if close > open:
                fun(open, close-1, temp + ")")
            
        fun(open, close, "")
        return res