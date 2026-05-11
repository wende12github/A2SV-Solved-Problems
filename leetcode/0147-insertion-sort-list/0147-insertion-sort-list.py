# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(val=-5000, next=head)
        l_sorted = head
        cur = head.next
        while cur:
            if cur.val >= l_sorted.val:
                l_sorted = l_sorted.next
            else:
                prev = dummy
                while prev.next.val <= cur.val:
                    prev = prev.next
                    
                l_sorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
                
            cur = l_sorted.next
            
        return dummy.next