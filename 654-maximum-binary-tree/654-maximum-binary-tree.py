# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        ind, maxi = 0, nums[0]
        for i in range(len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
                ind = i
                
        root = TreeNode(maxi)
        root.left = self.constructMaximumBinaryTree(nums[0:ind])
        root.right = self.constructMaximumBinaryTree(nums[ind+1:])
        
        return root
