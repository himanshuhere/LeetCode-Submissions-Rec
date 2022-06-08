
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    #same like list but in LL, find mid and operate
        def fn(head):
            if not head:    return None
            if not head.next:   return TreeNode(head.val)
            
            #find mid and devide lists
            pre = None
            sl = fs = head
            while fs and fs.next:
                pre = sl
                sl, fs = sl.next, fs.next.next
            pre.next = None
            
            root = TreeNode(sl.val)
            root.left = fn(head)
            root.right = fn(sl.next)
            
            return root
        
        return fn(head)