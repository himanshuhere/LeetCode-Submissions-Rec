#can use set directly their op (unorder) is o(1), but while random we need to convert it to list before takes o(n) thus no
#best way to keep a list and map, map for indexing so while removiing we can switch palces, and then randow.choice(arr) can be used, which will give same probability of return random
#inset - add ele to list if ele is not in list(check using map) then add map[ele] = n-1, since added at last place
#delete - now, check out the index of ele need to deleted, now take last element of list overwrite it to index element, update map and pop last one from list and deleted their key val pair from map.
#here duplicates are not allowed (as set), follow up if duplicates allowed how we gonna do? i mean one ele multiple indices think
        #insert     remove  random
#List - O(1)        N       1
#set    1/lg/n      1/lg/n  N
#DDL    1           N       N
#technically we need array so random can work on o(1), then wee need map so index-val lookup is o(1) so list+map

class RandomizedSet:

    def __init__(self):
        self.a , self.m = [], {}
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.m:   
            return False
        self.a.append(val)
        self.m[val] = self.n
        self.n += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.m:
            return False
        #see imp techninque
        idx = self.m[val]
        last = self.a[self.n - 1]
        
        self.a[idx] = last
        self.m[last] = idx
        
        self.a.pop()            #ye bhul hi gaya tha isliye wrong ans
        del self.m[val]
        self.n -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.a)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()