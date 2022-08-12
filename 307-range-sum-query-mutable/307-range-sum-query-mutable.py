#Basic prefix logic se toh TLE. 9/15 TC passed only.
#Read NOTES. I am making now segment tree recursive code

class TreeNode:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.left = None
        self.right = None
        self.sum = 0

class NumArray:
    def buildtree(self, arr, i, j):
        if i == j:
            root = TreeNode(i, j)
            root.sum = arr[i]
        else:
            mid = i + (j-i)//2
            root = TreeNode(i, j)
            root.left = self.buildtree(arr, i, mid)
            root.right = self.buildtree(arr, mid+1, j)
            root.sum = root.left.sum + root.right.sum
        return root
    
    def updatetree(self, root, index, val):
        if root.i == index == root.j:       #reached the correct leaf node
            root.sum = val
        else:
            mid = root.i + (root.j - root.i)//2
            if index <= mid:
                root.left = self.updatetree(root.left, index, val)
            else:
                root.right = self.updatetree(root.right, index, val)
            root.sum = root.left.sum + root.right.sum
        return root
    
    def sumrange(self, root, l, r):
        if root.i >=l and root.j <= r:
            return root.sum
        
        mid = (root.i+root.j)//2
        
        if r <= mid:
            return self.sumrange(root.left, l, r)
        elif l >=mid+1:
            return self.sumrange(root.right, l, r)
        else:                                       #overlapping with respact to mid think
            return self.sumrange(root.left, l, r) + self.sumrange(root.right, l, r)
    
    
    def __init__(self, nums: List[int]):
        self.root = self.buildtree(nums, 0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        self.updatetree(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.sumrange(self.root, left, right)


