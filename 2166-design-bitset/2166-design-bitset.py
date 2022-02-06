class Bitset:

    def __init__(self, size: int):
        self.bit = [0]*size
        self.countt = 0              #its very useful will save time in other fucntions
        self.flipp = False
        self.size = size

    def fix(self, idx: int) -> None:
        if not self.flipp:
            if self.bit[idx] == 0:
                self.bit[idx] = 1
                self.countt += 1
        else:                               #if flipped, so not in real so handle that way
            if self.bit[idx] == 1:
                self.bit[idx] = 0
                self.countt += 1
        

    def unfix(self, idx: int) -> None:
        if not self.flipp:
            if self.bit[idx] == 1:
                self.bit[idx] = 0
                self.countt -= 1
        else:                               #if flipped, so not in real so handle that way
            if self.bit[idx] == 0:
                self.bit[idx] = 1
                self.countt -= 1

    def flip(self) -> None:
        self.flipp = not self.flipp
        self.countt = self.size - self.countt         #1s count will invert so make sure

    def all(self) -> bool:
        return self.countt == self.size

    def one(self) -> bool:
        return self.countt >= 1

    def count(self) -> int:
        return self.countt

    def toString(self) -> str:
        s = ""
        if self.flipp:
            for idx in range(self.size):
                if self.bit[idx] == 1:
                    s+="0"
                else:
                    s+="1"
        else:                               #if flipped, so not in real so handle that way
            for idx in range(self.size):        
                if self.bit[idx] == 0:
                    s+="0"
                else:
                    s+="1"
        return s

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()