# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None

        # swap children of current node
        temp = root.left
        root.left = root.right
        root.right = temp

        # visit left and right children
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)       

        return root
