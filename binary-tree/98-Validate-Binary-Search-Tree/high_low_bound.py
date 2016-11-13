# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recursive(-float('inf'), root, float('inf'))
    def recursive(self, lowBound, node, highBound):
        if node == None:
            return True
        return node.val < highBound and node.val > lowBound and\
               self.recursive(lowBound, node.left, node.val) and self.recursive(node.val, node.right, highBound)
