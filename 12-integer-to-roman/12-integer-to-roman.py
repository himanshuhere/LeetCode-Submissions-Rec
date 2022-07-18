class Solution:
    def intToRoman(self, num: int) -> str:
        #1 both same
        rom = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        result = ""
        for n, v in rom.items():
            while num >= n:
                result += v
                num -= n
        return result
    
    
        #2
        rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        
        for i in range(len(val)):
            while num >= val[i]:
                result += rom[i]
                num -= val[i]
        return result
        
        #int to rom, me map me key int val roman bas bada map
        #rom to int, map me rom key val int, chota map
        