# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 1. split list into half using slow/fast pointer approach
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        secondHead = slow.next
        slow.next = None

        # 2. reverse the 2nd half of the list
        prev = None
        curr = secondHead
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. alternate adding nodes from left and right
        left = head
        right = prev
        
        while right != None:
            left_next, right_next = left.next, right.next
            left.next = right
            right.next = left_next
            left, right = left_next, right_next
