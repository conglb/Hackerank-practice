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


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''

def calc(u):
    v1 = v[0]
    v2 = v[1]
    count = 0
    if (u.info == v1):
        count += 1
    if (u.info == v2):
        count += 1
    if u.left != None:
        count += calc(u.left)
    if u.right != None:
        count += calc(u.right)
    return count


def lca(root, v1, v2):
    lca = root
    haveNewRes = True
    while haveNewRes:
        haveNewRes = False
        if (lca.left != None):
            if calc(lca.left) == 2:
                haveNewRes = True
                lca = lca.left
                continue
        if (lca.right != None):
            if calc(lca.right) == 2:
                haveNewRes = True;
                lca = lca.right
                continue
    return  lca


# Enter your code here

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)

