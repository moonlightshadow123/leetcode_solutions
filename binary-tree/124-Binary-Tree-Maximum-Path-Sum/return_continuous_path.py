# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum =- float('inf')
        self.findMax(root)
        return self.maxSum
    
    def findMax(self, root):
        if root == None:
            return 0
        maxLeft = self.findMax(root.left)
        maxRight = self.findMax(root.right)
        self.maxSum = max(maxRight+maxLeft+root.val, self.maxSum)
        return max(0, root.val, root.val+maxLeft, root.val+maxRight)
