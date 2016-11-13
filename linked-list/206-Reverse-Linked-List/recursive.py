# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        tail = head
        while tail.next != None:
            tail = tail.next
        self.reverse(head)
        return tail
    def reverse(self, node):
        if node == None:
            return None
        newTail = self.reverse(node.next)
        if newTail != None:
            newTail.next = node
        node.next = None
        return node
