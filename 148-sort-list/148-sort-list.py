# The problem is to sort the linked list in O(nlogn) time and using only constant extra space. If we look at various sorting algorithms, Merge Sort is one of the efficient sorting algorithms that is popularly used for sorting the linked list. The merge sort algorithm runs in O(nlogn) time in all the cases. Let's discuss approaches to sort linked list using merge sort.

# Quicksort is also one of the efficient algorithms with the average time complexity of O(nlogn). But the worst-case time complexity is O(n^2). Also, variations of the quick sort like randomized quicksort are not efficient for the linked list because unlike arrays, random access in the linked list is not possible in O(1) time. If we sort the linked list using quicksort, we would end up using the head as a pivot element which may not be efficient in all scenarios.


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #MERGE SORT
        def merge(l, r):
            dummy = p = ListNode(0)
            while l and r:
                if l.val > r.val:
                    p.next = r
                    r = r.next
                else:
                    p.next = l
                    l = l.next
                p = p.next
            p.next = l or r
            return dummy.next
    
        
        if not head or not head.next:
            return head
        
        #Find the middle to devide
        pre = ListNode(None)
        sl, fs = head, head
        while fs and fs.next:
            pre = sl
            sl = sl.next
            fs = fs.next.next
        pre.next = None
        
        #call recursive for smaller length
        l = self.sortList(head)
        r = self.sortList(sl)
        
        return merge(l, r)
    
        