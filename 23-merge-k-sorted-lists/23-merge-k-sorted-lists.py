
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # The above solution works fine with Python 2.However, with Python3 it gives Type Error:
        # TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
        # This error occurs because the cmp() special method is no longer honored in Python 3

        ListNode.__eq__ = lambda a,b: a.val == b.val
        ListNode.__lt__ = lambda a,b: a.val < b.val
        
    #2 O(nlogk) still otimized
        h = []
        for each_head in lists:
            if each_head:
                heapq.heappush(h, (each_head.val, each_head))   #only first node, since inner arr itself sorted
        
        dummy = head = ListNode(0)
        while h:
            x = heapq.heappop(h)[1]
    
            if x.next:
                heapq.heappush(h, (x.next.val, x.next))
            
            head.next = x
            head = head.next

        return dummy.next
    
    
    #1 o(nlogk)
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r): #l and r are two list tho l and r are working as head1 and head2 for both list
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next
        
