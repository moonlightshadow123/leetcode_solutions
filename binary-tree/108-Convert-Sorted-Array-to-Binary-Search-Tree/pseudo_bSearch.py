# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.index = 0
        return self.toBST(nums, 0, len(nums)-1)
        
    def toBST(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        # node = TreeNode(nums[mid])
        leftNode = self.toBST(nums, start, mid - 1)
        node = TreeNode(nums[self.index])
        self.index += 1
        rightNode = self.toBST(nums, mid + 1, end)
        node.left = leftNode
        node.right = rightNode
        return node
