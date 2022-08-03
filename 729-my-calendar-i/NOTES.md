class Node:             #Python treemap
def __init__(self, st, end):
self.st = st
self.end = end
self.left = None
self.right = None
def insert(self, node_st, node_end):             #root, node
if node_end <= self.st:
if not self.left:
self.left = Node(node_st, node_end)        #inserted
return True
return self.left.insert(node_st, node_end)
elif node_st >= self.end:
if not self.right:
self.right = Node(node_st, node_end)        #inserted
return True
return self.right.insert(node_st, node_end)
else:
return False               #overlapping
​
class MyCalendar:
def __init__(self):
self.root = None
def book(self, st, end):
if self.root == None:
self.root = Node(st, end)
return True
return self.root.insert(st, end)
​