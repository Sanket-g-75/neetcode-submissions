# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head is None or head.next is None or head.next.next is None:
            return

        curr = head
        second = curr.next

        while curr.next.next is not None:
            curr = curr.next

        last = curr.next
        curr.next = None

        head.next = last
        last.next = second

        self.reorderList(head.next.next)


        
