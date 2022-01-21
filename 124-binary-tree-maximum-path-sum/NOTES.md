#just like aditya diameter concept will lil focus on cases as HARD it is
​
def dfs(root):
if not root:
return 0
l, r = dfs(root.left), dfs(root.right)
#Induction
self.res = max(self.res, l + r + root.val)
return max(root.val + max(l, r), 0)
self.res = -math.inf
dfs(root)
return self.res