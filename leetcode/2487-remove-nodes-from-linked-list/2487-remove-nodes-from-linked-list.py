# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        while current:
            stack.append(current)
            current = current.next

        temp_node = stack.pop()
        while stack:
            while stack and stack[-1].val < temp_node.val:
                stack.pop()
                
            if stack:
                new_node = stack.pop()
                new_node.next = temp_node
                temp_node = new_node

        return temp_node