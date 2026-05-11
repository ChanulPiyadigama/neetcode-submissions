# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        length = 0
        while start:
            length+=1
            start= start.next

        nodeRemoveIdx = length - n
        print(nodeRemoveIdx)
        prev, curr = None, head
        while True:
            if nodeRemoveIdx == 0:
                if prev:
                    prev.next = curr.next
                    curr.next = None
                else:
                    return curr.next
                break
            else:
                nodeRemoveIdx-=1
                prev = curr
                curr = curr.next
        return head