# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # reached an empty node, can't say there's a mismatch
        if not p and not q:
            return True
        # node is missing or the values are different --> definitely not same tree
        if not q or not p or (p.val != q.val):
            return False
        # recursively check left and right children
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        
