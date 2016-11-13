# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        p = dummy.next
        while p != None and p.next != None:
            n = p.next
            nn = n.next
            prev.next = n
            n.next = p
            p.next = nn
            prev = p
            p = nn
        return dummy.next
