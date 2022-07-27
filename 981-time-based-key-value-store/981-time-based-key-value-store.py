#We need exact timestamp value from the [key]-> list, if not then the closest smaller one. Okay we can apply binary search but wait sorting it and then applyting binary gonna cost nlogn, better we can go for linear search. Yes, but now see constraints
#All the timestamps timestamp of set are strictly increasing. - > means your list wll automatically be sorted by given input, now you just need to apply binary search there.
#This is very good question to actually ask in interview wether coming timestamps be greater than previous or not.


class TimeMap:

    def __init__(self):
        self.store = {} #key : str -> val : [ list for tuples (val, timetsamp)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        space = self.store.get(key, [])
        res = ""
        
        l, r = 0 , len(space)-1
        while l <= r:
            m = (l+r)//2
            if space[m][1] <= timestamp:
                res = space[m][0]
                l = m+1
            else:
                r = m-1
        return res
        
        
        
        
        
        #template 2, but need some checks
        while l < r:
            m = ((l+r)//2) + 1      #biasing to the right side, better use <= template
            if space[m][1] > timestamp:
                r = m-1
            else:
                l = m
        res = space[l]
        if res[1] <= timestamp:
            return res[0]
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)