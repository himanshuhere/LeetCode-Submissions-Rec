#READ NOTES PLS
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.s = []
        while root:
            self.s += [root]
            root = root.left

    def next(self) -> int:
        node = self.s.pop() #return to isiko karna hai but usse pehle next snammest ki vyavastha karke jana isliye cur step kuki next smallest ek right aur uske sidhe sare left most me hai 
        cur = node.right
        
        while cur:
            self.s += [cur]
            cur = cur.left
            
        return node.val

    def hasNext(self) -> bool:
        return len(self.s) > 0

#now see 653
    
    
    
    
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()