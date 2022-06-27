class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #there are two ways, go preorder and go postorder.
        #if preorder, you can either put camera at root or its chidrens and go on. Here putting at root would be greedly better way right as childs are gonna be more that root max 2.
        #If postorder, either we can put cameras at all leaves or to their partents. And see putting camera at leaves parent will cover leaves as well as their parent too, which leaves wont do if put at them. Plus leaves parent will alwys be lesser that leaves and more beneficial as per condition. 
        #So we grt the best approach, do postorder and put cameras at leaves parent.
        
        # 0 means not covered。1 means covered but not has a camera on it. 2 means a camera on it.
        # reference: https://www.itread01.com/content/1546174153.html
        def dfs(node):
            if not node:
                return 1        #so. at leaf you return 0, skipping leaf (see else)
            
            l=dfs(node.left)
            r=dfs(node.right)
            
            if l==0 or r==0:        #leaf's parent
                self.sum+=1
                return 2
            elif l==2 or r==2:
                return 1
            else:
                return 0            
        
        self.sum=0
        if dfs(root) == 0:
            self.sum+=1     #putting at root, if not there
        
        return self.sum
