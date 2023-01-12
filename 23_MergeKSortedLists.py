# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # handle edge cases
        if lists == None or len(lists) == 0:
            return None
        
        # keep merging two lists together
        # store intermediate results and use that as the new working list each loop
        # merging two lists is easy, done in LC 21 (easy)
        while len(lists) > 1:
            intermediateLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None # l2 might be out of bounds
                mergedList = self.mergeTwoLists(l1, l2)
                intermediateLists.append(mergedList)
            lists = intermediateLists
        return lists[0]

    # exactly the same code as LC 21
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next
