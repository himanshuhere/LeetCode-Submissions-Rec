class Solution:
    def romanToInt(self, s: str) -> int:
        #sidha logic hai, roman me l to r apana bade se chote jate hai like MCLXV something like thisn but exception kaha hai ese MDXIV, MXCIV, jab dip aata hai try to plot graph. #Apan piche se aage aate jayege agar sab kuch bada milta gaya to add it like it is agat bade k bad chota mila then this is a value composed of two char like IV, XL, so we make 4, 40
        
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        res, prev = dict[s[-1]], dict[s[-1]]
        
        for i in range(len(s)-2, -1, -1):          # rev the s
            cur = s[i]
            if dict[cur] >= prev:
                res += dict[cur]              # sum the value iff previous value same or more
            else:   
                res -= dict[cur]              # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
            prev = dict[cur]
        return res