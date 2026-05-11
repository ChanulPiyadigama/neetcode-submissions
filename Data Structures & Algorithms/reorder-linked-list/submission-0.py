# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = start = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next   

        curr = slow.next
        slow.next = None
        prev = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 

        while start != prev and start.next != prev:
            startTemp = start.next
            start.next = prev
            start = startTemp

            prevTemp = prev.next
            prev.next = start
            prev = prevTemp
        
            