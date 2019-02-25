# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''


def height(root):
    if root.left == root.right == None:
        return 0
    h = 0
    if root.left != None:
        h = root.left + 1
    if root.right != None:
        h = max(h, root.right + 1)
    return h

