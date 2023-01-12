# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # recursive depth first search
        # get the max height of the subtrees and add the node's own height (1)
        # by far the simplest and fastest solution
        # but other approaches worth understanding
        """
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        """

        # iterative breadth first search
        # add nodes to a queue level-by-level
        # return once there are no more levels
        """
        if root == None:
            return 0
        level = 0
        q = collections.deque([root])
        while len(q) > 0:
            for i in range(len(q)):
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            level += 1
        return level
        """

        # iterative depth first search
        # use a stack to store the node and its depth
        # add node's children to stack
        if root == None:
            return 0
        maxHeight = 1
        stack = collections.deque([(root, maxHeight)])
        while len(stack) > 0:
            node, height = stack.pop()
            maxHeight = max(maxHeight, height)
            if node.left != None:
                stack.append((node.left, height + 1))
            if node.right != None:
                stack.append((node.right, height + 1))
        return maxHeight
