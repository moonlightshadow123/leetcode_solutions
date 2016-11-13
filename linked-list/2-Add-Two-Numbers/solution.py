# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p = head
        carry = 0
        while l1 != None or l2 != None:
            digitSum = self.getVal(l1) + self.getVal(l2) + carry
            carry = digitSum / 10
            digit = digitSum % 10
            p.next = ListNode(digit)
            l1 = None if l1 == None else l1.next
            l2 = None if l2 == None else l2.next
            p = p.next
        if carry == 1:
            p.next = ListNode(1)
        return head.next
        
    def getVal(self, node):
        if node == None:
            return 0
        else:
            return node.val
