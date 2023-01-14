# MY FIRST ATTEMPT - 51/52 test cases, just not fast enough
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # 1. Level order traversal
        if not root:
            return " "
        level = list([root])
        res = ""
        while len(level) > 0:
            nextLevel = []
            actualNodeAdded = False
            for node in level:
                if node:
                    actualNodeAdded = True
                    res += str(node.val) + "#"
                    if node.left:
                        nextLevel.append(node.left)
                    else:
                        nextLevel.append(None)
                    if node.right:
                        nextLevel.append(node.right)
                    else:
                        nextLevel.append(None)
                else:
                    res += "null#"
                    nextLevel.append(None)
                    nextLevel.append(None)
                      
            if actualNodeAdded == False:
                break
            level = nextLevel
        # at this point, res should resemble:
        # "1#2#3#null#null#4#5#"
        
        return res[0 : len(res) - 1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split("#")
        if vals == None or vals[0] == "null" or vals[0] == " ":
            return None
        root = TreeNode(vals[0])
        
        def buildTree(root, vals, i):
            if not root:
                return None
            if 2 * i + 1 >= len(vals) or vals[2 * i + 1] == "null":
                root.left = None
            else:
                root.left = TreeNode(vals[2 * i + 1])
            if 2 * i + 2 >= len(vals) or vals[2 * i + 2] == "null":
                root.right = None
            else:
                root.right = TreeNode(vals[2 * i + 2])
            root.left = buildTree(root.left, vals, 2 * i + 1)
            root.right = buildTree(root.right, vals, 2 * i + 2)

            return root
        
        root = buildTree(root, vals, 0)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
"""


