# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums)-1)
    
    def build(self, nums, low, high):
        if low > high:
            return None
        mid = (low+high)//2
        node = TreeNode(nums[mid])
        node.left = self.build(nums, low, mid-1)
        node.right = self.build(nums, mid+1, high)
        return node