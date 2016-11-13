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
        self.curNode = head
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        return self.toBST(0, n-1)
    def toBST(self, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        #######################
        leftNode = self.toBST(start, mid-1)
        #######################
        node = TreeNode(self.curNode.val)
        self.curNode = self.curNode.next
        rightNode = self.toBST(mid+1, end)
        #######################
        node.left = leftNode
        node.right = rightNode
        return node
        
        
