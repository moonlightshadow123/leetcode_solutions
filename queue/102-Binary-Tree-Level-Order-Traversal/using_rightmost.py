# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = [root]
        res = []
        curLevel = []
        rightmost = root
        while len(queue) != 0:
            curNode = queue[0]
            del queue[0]
            curLevel.append(curNode.val)
            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)
            if curNode == rightmost:
                res.append(curLevel)
                if len(queue) != 0:
                    rightmost = queue[-1]
                    curLevel = []
        return res
