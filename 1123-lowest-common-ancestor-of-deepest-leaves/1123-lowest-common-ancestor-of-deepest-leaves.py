class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #to decide levels of nodes
#         def height(r):
#             if not r:
#                 return 0
#             l, r = dfs(r.left), dfs(r.right)
#             return max(l, r) + 1            #means leaf nodes is at level 1
#this, function doing two things parallely - deciding on levels and sange deciding on LCA.
# fo if both branch is of same height then root is lca else if left is bigger LCA is from the left side, might be this could change on more upper side. dont get cofuse thats y put level code first then merged code. it is base, hypothesis and induction step only or if you see it is modified LCA only. but u need to understand ques first, if any of the leaf is more deeper then that is LCA of itselft thats why l>r return left and if two leaf are at same level the their ultimate root is the LCA
#input = [1234] , Since the set contain only one deepest leaf i.e [4], so its lca is node itself.
    
    #you could make height function separate then call it every time from dfs yes o(n^2), but it will send your idea in simpler way to interview so dont jump directly on merged def. better first o(n^2) then o(n) on doing same thing in one function using tuples/pair
        def dfs(r):
            if not r:
                return (r, 0)
            
            left, l_lev = dfs(r.left)
            right, r_lev = dfs(r.right)
            
            if l_lev == r_lev:      #then , i am the  LCA
                return (r, l_lev + 1)
            
            if l_lev > r_lev:       #LCA should come from left
                return (left, l_lev + 1)
            
            else:                   #LCA should come from right
                return (right, r_lev + 1)
        
        LCA, lev = dfs(root)
        return LCA