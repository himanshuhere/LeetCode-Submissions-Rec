# class MyCalendar:

    #1. brute workd with set, but jaha tak i know ye series sayd seg tree me hai #o(n^2)
#     def __init__(self):
#         self.bookings = set()

#     def book(self, st: int, end: int) -> bool:
#         if (st, end) in self.bookings:
#             return False
#         for u, v in self.bookings:
#             if not (v<=st or end<=u):
#                 return False
#         self.bookings.add((st, end))
#         return True
    
    #2 - dekho mene dekha and socha yes ordered set ho to binary search laga sakte. but like java  we dont have any tree map. So what we ll create wese b bahot contest me bc haara hu kuki treemap nhi pata tha pythn ka aur unko complexity logn chaiye rehti this to lo template aaj.
    
#total time for all N queries: O(N^2) worst case, with O(NlogN) on random data.
#total time : o(N)

class Node:             #Python treemap | TC : o(n) skewed case, random elements logn
    def __init__(self, st, end):
        self.st = st
        self.end = end
        self.left = None
        self.right = None
    
    def insert(self, node_st, node_end):             #root, node
        if node_end <= self.st:
            if not self.left:
                self.left = Node(node_st, node_end)        #inserted
                return True
            return self.left.insert(node_st, node_end)
        elif node_st >= self.end:
            if not self.right:
                self.right = Node(node_st, node_end)        #inserted
                return True
            return self.right.insert(node_st, node_end)
        else:
            return False               #overlapping 

class MyCalendar:
    def __init__(self):
        self.root = None
    
    def book(self, st, end):
        if self.root == None:
            self.root = Node(st, end)
            return True
        return self.root.insert(st, end)
    
