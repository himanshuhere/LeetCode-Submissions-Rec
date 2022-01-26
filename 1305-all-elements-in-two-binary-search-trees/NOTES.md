#inorder
def dfs(r):
if not r:
return
dfs(r.left)
res.append(r.val)
dfs(r.right)
res = []
dfs(root1)
dfs(root2)
return sorted(res)
#optimal wud be to use inorder and get two sorted list, then merge then in o(n) rather sorting