# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # my first solution
        """
        # 1. reverse list
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 2. come back and un-reverse list and remove node in process
        if n == 1:
            prev = prev.next
        curr = prev
        prev = None
        index = 1
        while curr:
            if index + 1 == n:
                nxt = curr.next.next
            else:
                nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            index += 1

        return prev
        """

        # two pointer solution - only requires one pass
        dummy = ListNode()
        dummy.next = head
        lag = dummy
        lead = head
        steps = 0
        while steps < n:
            lead = lead.next
            steps += 1
        while lead:
            lag = lag.next
            lead = lead.next
        lag.next = lag.next.next
        return dummy.next
