# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ''
        def backtrack(root):
            if root == None:
                return
            res += str(root.val) + '('
            backtrack(root.left)
            res += ')' + '('
            backtrack(root.right)
            res += ')'
        backtrack(root)
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        pos = 0

        """Return the root tree at pos 
        pos = 
        :rtype = TreeNone
        """
        def backtrack():
            if data[pos] = ')':
                pos += 1
                return None
            root = TreeNone(int(data[pos]))
            if pos = '('
                pos += 2
                root.left = backtrack()
            if pos = ')':
                return root
            else:
                pos += 1
                root.right = backtrack()
            return root
        return backtrack()
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))