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
        dummy.next = self.recursive(head)
        return dummy.next
    def recursive(self, node):
        if node == None or node.next == None:
            return node
        p = node.next
        node.next = self.recursive(p.next)
        p.next = node
        return p
