class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_ = {
            '0' : '0',
            '1' : '1',
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        result = []
        
        if not len(digits):
            return []
        
        #backtracking
        def fun(i, temp):
            if i == len(digits):
                result.append(''.join(temp))
                return
            
            curr_s = map_[digits[i]]
            
            for k in range(len(curr_s)):
                temp.append(curr_s[k])
                fun(i+1, temp)
                temp.pop()
        ###########
        
        fun(0, [])
        
        return result