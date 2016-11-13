# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.maxDepth(root) != -1
    def maxDepth(self, node):
        if node == None:
            return 0
        leftDepth = self.maxDepth(node.left)
        rightDepth = self.maxDepth(node.right)
        if leftDepth == -1 or rightDepth == -1:
            return -1
        elif abs(leftDepth - rightDepth) > 1:
            return -1
        else:
            return max(leftDepth, rightDepth) + 1
