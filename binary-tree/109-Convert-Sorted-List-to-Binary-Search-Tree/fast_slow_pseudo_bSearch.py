# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.toBST(head, None)
    def toBST(self, startNode, endNode):
        if startNode == endNode:
            return None
        fast = startNode
        slow = startNode
        while fast.next != endNode and fast.next.next != endNode:
            fast = fast.next.next
            slow = slow.next
        node = TreeNode(slow.val) 
        node.left = self.toBST(startNode, slow)
        node.right = self.toBST(slow.next, endNode)
        return node
        
        
