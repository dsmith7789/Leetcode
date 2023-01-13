# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        # first approach: recursion to implement in-order traversal
        # store elements in an array
        """
        elements = self.inOrderTraversal(root, [])
        return elements[k - 1]

    def inOrderTraversal(self, root, elements):
        # add left
        if root.left:
            elements = self.inOrderTraversal(root.left, elements)
        
        # add self
        elements.append(root.val)

        # add right
        if root.right:
            elements = self.inOrderTraversal(root.right, elements)

        return elements
        """

        # second approach: iterative (sort of replicate the call stack)
        # in our own stack
        stack = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            current = current.right
