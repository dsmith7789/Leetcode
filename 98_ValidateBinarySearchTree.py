# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # root has no restrictions on range, 
        # but range is updated as we traverse the tree
        return self.valid(root, float("-inf"), float("inf"))
    
    def valid(self, node, leftBound, rightBound):
        if not node:
            return True
        if node.val <= leftBound or node.val >= rightBound:
            return False

        # go left -> update rightBound
        # go right -> update leftBound
        return self.valid(node.left, leftBound, node.val) and \
               self.valid(node.right, node.val, rightBound)
