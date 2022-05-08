def dfs(nested, flat):
    for elem in nested:
        if elem.isInteger():
            flat.append(elem.getInteger())
        else:
            dfs(elem.getList(), flat)

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flatList, self.i = [], 0
        dfs(nestedList, self.flatList)
    
    def next(self) -> int:
        self.i += 1
        return self.flatList[self.i-1]
    
    def hasNext(self) -> bool:
        return self.i < len(self.flatList)
    

    
    
    
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
        
    def next(self):
        return self.stack.pop().getInteger()
        
    def hasNext(self):
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False