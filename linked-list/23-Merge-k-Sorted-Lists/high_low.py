# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        start = 0
        end = len(lists) - 1
        while end != 0:
            start = 0
            while start < end:
                lists[start] = self.merge2lists(lists[start], lists[end])
                start += 1
                end -= 1
        return lists[0]
    
    def merge2lists(self, l1, l2):
        dummy = ListNode(0)
        p = dummy
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1 == None:
            p.next = l2
        if l2 == None:
            p.next = l1
        return dummy.next
            
