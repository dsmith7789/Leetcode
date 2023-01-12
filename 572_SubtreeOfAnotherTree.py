# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
        


    # took from LC 100: Same Tree
    def isSameTree(self, p, q):
        # reached an empty node, can't say there's a mismatch
        if not p and not q:
            return True
        # node is missing or the values are different --> definitely not same tree
        if not q or not p or (p.val != q.val):
            return False
        # recursively check left and right children
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
