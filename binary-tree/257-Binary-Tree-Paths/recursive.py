# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.pathRecd = []
        if root == None:
            return self.pathRecd
        self.findPath(root, str(root.val))
        return self.pathRecd
    def findPath(self, root, pathString):
        if root.left == None and root.right == None: 
            self.pathRecd.append(pathString)
        if root.left != None:
            self.findPath(root.left, pathString+'->'+str(root.left.val))
        if root.right != None:
            self.findPath(root.right, pathString+'->'+str(root.right.val))
