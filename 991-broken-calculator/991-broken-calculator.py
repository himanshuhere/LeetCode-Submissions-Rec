class Solution:
    def brokenCalc(self, s: int, t: int) -> int:
            op = 0
            while t > s:
                if t & 1:   t += 1
                else:       t >>= 1
                op += 1
            return op + (s - t)
                
        #I would like to add some explanations for working backwards:
#If with subtraction and multiplication, the effect of earlier subtraction will be amplified by later multiplications, hence, greedily doing multiplication might not reach optimal solution as an additional early subtraction can have a huge effect.
#Whereas with addition and division, earlier addition will be diminished by later divisions. It is thus always better to do division wherever possible.

#We can also think about it this way. From X to Y, the only way to go is either -1 or x2. Any such path leading to Y also means that there exists a path from Y back to X through +1 or /2. The key is that going from X to Y is not deterministic, because one can choose to x2, or -1 first and then x2. However, going from Y to X is deterministic, because we cannot do /2 when Y is an odd number. Therefore, whenever Y is an odd number, the only thing we can do is +1 and then /2. Therefore, going from Y to X is straightforward.
#         op = 0
#         while True:
#             if s == t:
#                 return op
            
#             if s*2 <= t+1:
#                 s = s*2
#             else:
#                 s -= 1
#             op += 1

            
