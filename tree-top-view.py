class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    left = []
    right = []
    def dfs(root, pos):
        if pos < 0:
            if -pos > len(left):
                left.append(root.info)
        if root.left != None:
            dfs(root.left, pos - 1)
        if root.right != None:
            dfs(root.right, pos + 1)
    def dfs2(root, pos):
        if pos > 0:
            if pos > len(right):
                right.append(root.info)
        if root.right != None:
            dfs2(root.right, pos + 1)
        if root.left != None:
            dfs2(root.left, pos - 1)
    dfs(root, 0)
    dfs2(root, 0)
    for num in reversed(left):
        print(num, end=' ')
    print(root.info, end=' ')
    for num in right:
        print(num, end= ' ')


# Write your code here


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)