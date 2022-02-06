class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #just flip maths
        # [ 0, 1, 0, 0, 1, 1, 0] --> original
        # [ 0, 1, 1, 0, 0, 1, 0]  -> flipped
        # [ 1, 0, 0, 1, 1, 0, 1]  -> inverted 
        # see, 0 + 0 = 1, 1 + 1 =0, 0 + 1 = 0, 1 + 0 = 1
        # thus if same , put 1- n else n
        
        #invert = 1-bit or 1^bit
        
        for words in image:
            
            l, r = 0, len(words) - 1
            while l <= r:
                if words[l] == words[r]:
                    words[l] = words[r] = 1 - words[l] #invert the bit
                l += 1
                r -= 1
                
        return image
    
    
    #kuch mat karo, u know do iter nhi karna to sidha rough me input likho niche output likho, nowu ll see diff. pehle tum in output bit compare karoge dekhoge kahi 0-0 1-1 hai to kahi 0-1 1-0, dikkat hai ab vertical compare to nhi nikal rha kcuh now see horizotal kese two pointer jese(ye idea kaha se aaya bhai reverse se revsere ignore mat karo time bachao but dont ignore) 
    #clear ho jayega ki i==j hai to invert kardo bits (1-n or 1^n) agar i!=j to wesa rehne do, 2-3 test case me dekho.
    #bas i++ j-- dono me hoga
        