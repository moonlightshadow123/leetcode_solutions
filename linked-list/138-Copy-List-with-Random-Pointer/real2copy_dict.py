# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        real2copydict = {None:None}
        dummy = RandomListNode(0)
        p = head
        q = dummy
        while p != None:
            node = RandomListNode(p.label)
            real2copydict[p] = node
            q.next = node
            p = p.next
            q = q.next
        p = head
        q = dummy.next
        while p != None:
            q.random = real2copydict[p.random]
            p = p.next
            q = q.next
        return dummy.next
        
