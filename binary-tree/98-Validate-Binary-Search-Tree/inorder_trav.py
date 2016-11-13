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
        self.prev = None
        return self.isMonotonicIncreasing(root)
    
    def isMonotonicIncreasing(self, node):
        if node == None:
            return True
        if not self.isMonotonicIncreasing(node.left):
            return False
        if self.prev != None and self.prev.val >= node.val:
            return False
        self.prev = node
        if not self.isMonotonicIncreasing(node.right):
            return False
        return True
